terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

# Configure the Docker provider
provider "docker" {
  host = "unix:///var/run/docker.sock"
  # For Windows, use "npipe:////.//pipe//docker_engine"
}

# Pull an image
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

# Run a container
resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial-container"
  ports {
    internal = 80
    external = 8000
  }
}
