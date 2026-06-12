resource "google_compute_network" "gke_vpc" {
  name                    = "bouldering-gke-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "gke_subnet" {
  name          = "bouldering-gke-subnet"
  region        = "europe-central2"
  network       = google_compute_network.gke_vpc.name
  ip_cidr_range = "10.10.0.0/24"
}