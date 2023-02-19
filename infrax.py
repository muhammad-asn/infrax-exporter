from service.docker import DockerService
from service.elasticsearch import ElasticsearchService
from service.kibana import KibanaService
from service.java import JavaService
from service.python import PythonService
from service.nodejs import NodeJsService
from prometheus_client import (
    Gauge,
    start_http_server,
    REGISTRY,
    GC_COLLECTOR,
    PLATFORM_COLLECTOR,
    PROCESS_COLLECTOR,
)

import time
import os


class InfraX_Exporter:
    def __init__(self, name: str):
        services = {
            "docker": DockerService(),
            "elasticsearch": ElasticsearchService(
                addr=os.getenv("ELASTICSEARCH_HOST", "localhost:9200")
            ),
            "kibana": KibanaService(),
            "java": JavaService(),
            "python": PythonService(),
            "nodeJs": NodeJsService(),
        }
        self.name = name
        self.service = services.get(name)
        if self.service is None:
            raise NameError("Service is not recognized.")

        self.service_info = Gauge(
            f"{self.name}_service_info",
            f"{self.name.title()} platform information",
            ["current_version", "latest_version"],
        )

    def collect_metric(self) -> None:
        self.service_info.labels(
            current_version=self.service.get_current_version(),
            latest_version=self.service.get_latest_version(),
        )


if __name__ == "__main__":
    REGISTRY.unregister(GC_COLLECTOR)
    REGISTRY.unregister(PLATFORM_COLLECTOR)
    REGISTRY.unregister(PROCESS_COLLECTOR)
    docker = InfraX_Exporter("docker")
    elasticsearch = InfraX_Exporter("elasticsearch")

    start_http_server(8001)
    while True:
        docker.collect_metric()
        elasticsearch.collect_metric()
        time.sleep(30)
