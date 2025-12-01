
resource "googgle_compute_instance" "some_name_here" {
  name    = instance_name_here
  project = project_id_here
  zone    = zone_here
  machine_type = "e2-medium" # for example
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      }
  }
  network_interface {
    network = "default"
  }
}
