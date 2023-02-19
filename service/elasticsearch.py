from service.base import InfraService
import subprocess, json, re


class ElasticsearchService(InfraService):
    def __init__(self, addr):
        self.addr = addr

    def get_current_version(self):
        command = f"curl -sSL {self.addr}"
        current_version = json.loads(
            subprocess.check_output(command, shell=True).decode()
        )
        return current_version["version"]["number"]

    def get_latest_version(self):
        command = "curl -sSL https://www.elastic.co/downloads/elasticsearch"
        output = subprocess.check_output(command, shell=True).decode()
        latest_version = (
            re.search(r"Elasticsearch \d+\.\d+\.\d+", output).group(0).split()[-1]
        )
        return latest_version
