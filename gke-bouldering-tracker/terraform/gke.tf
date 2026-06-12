resource "google_container_cluster" "primary" {
  name     = "bouldering-cluster"
  location = "europe-central2-a"

  remove_default_node_pool = true
  initial_node_count       = 1

  network    = google_compute_network.gke_vpc.name
  subnetwork = google_compute_subnetwork.gke_subnet.name

  deletion_protection = false
}

resource "google_container_node_pool" "spot_nodes" {
  name       = "spot-node-pool"
  location   = "europe-central2-a"
  cluster    = google_container_cluster.primary.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "e2-small"

    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
