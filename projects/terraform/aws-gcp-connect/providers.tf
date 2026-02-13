
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0"
    }
    google = {
      source = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  access_key = file("aws-creds/aws_access_key.txt")
  secret_key = file("aws-creds/aws_secret_key.txt")
}

provider "google" {
  project = file("gcp-creds/gcpproject.txt")
  credentials = file("gcp-creds/aws-gcp.json")
}
