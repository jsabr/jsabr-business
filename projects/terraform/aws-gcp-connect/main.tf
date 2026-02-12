
resource "aws_vpc" "main" {
  cidr_block = 10.1.0.0/16
}

resource "google_compute_network" "vpc_network" {
  name = "public-demo-network"
}