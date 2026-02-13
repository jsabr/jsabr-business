output "aws_vpc_id" {
  value = aws_vpc.main.id
}

output "gcp_network_id" {
  value = google_compute_network.vpc_network.id
}