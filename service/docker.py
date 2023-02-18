from service.base import InfraService
import docker
import subprocess


class DockerService(InfraService):
    def __init__(self):
        self.client = docker.from_env()

    def get_current_version(self):
        return self.client.version().get("Version")

    def get_latest_version(self):
        command = "curl -sSL https://download.docker.com/linux/static/stable/x86_64/ | grep -E -o '[0-9]+\.[0-9]+\.[0-9]+' | sort -r | head -n 1"
        latest_version = subprocess.check_output(command, shell=True).decode().strip()
        return latest_version
