from service.base import InfraService
import docker
import subprocess
import re


class DockerService(InfraService):
    def __init__(self):
        self.client = docker.from_env()

    def get_current_version(self) -> str:
        current_version = self.client.version().get("Version")
        return current_version

    def get_latest_version(self) -> str:
        command = "curl -sSL https://download.docker.com/linux/static/stable/x86_64/"
        html_output = subprocess.check_output(command, shell=True).decode().strip()
        pattern = r'href="docker-([0-9]+\.[0-9]+\.[0-9]+)\.tgz"'
        version_numbers = re.findall(pattern, html_output)
        latest_version = sorted(version_numbers, reverse=True)[0]
        return latest_version
