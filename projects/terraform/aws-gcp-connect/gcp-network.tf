resource "google_compute_network" "vpc_network" {
  name                    = "poc-gcp-network"
  auto_create_subnetworks = false # Standard practice for clean architecture
}

resource "google_compute_subnetwork" "public" {
  name          = "poc-gcp-subnetwork"
  ip_cidr_range = "10.1.1.0/24"
  region        = "us-central1"
  network       = google_compute_network.vpc_network.id
}