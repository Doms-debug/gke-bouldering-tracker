terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "prj-cloud-sandbox-repo"
  region  = "europe-central2"
  zone    = "europe-central2-a"
}
