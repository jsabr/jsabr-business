
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
  access_key = trimspace(file("aws_access_key.txt"))
  secret_key = trimspace(file("aws_secret_key.txt"))
}

provider "google" {
  project = var.gcp_project_id
  credentials = file("my-gcp-key.json")
}
