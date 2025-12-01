terraform { 
  required_version = ">1.4.0"
  backend "local"  = {
    path   = "terraform/state/terraform.tfstate"
    }
}

provider "google" {
  project  = var.project_id
  region   = var.region
  zone     = var.zone
}

module "instances" {
  source = "./modules/instances"
}
