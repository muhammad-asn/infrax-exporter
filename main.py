from service.docker import DockerService
from service.elasticsearch import ElasticsearchService
from service.kibana import KibanaService
from service.java import JavaService
from service.python import PythonService
from service.nodejs import NodeJsService
from prometheus_client import start_http_server, Gauge
import time

docker_service_info = Gauge(
    "docker_service_info", "Docker platform information", ["current_version", "latest_version"]
)
elasticsearch_info = Gauge(
    "elasticsearch_service_info",
    "Elasticsearch platform information",
    ["current_version", "latest_version"],
)
kibana_info = Gauge(
    "kibana_service_info", "Kibana platform information", ["current_version", "latest_version"]
)
java_info = Gauge(
    "java_service_info", "Java platform information", ["current_version", "latest_version"]
)
python_info = Gauge(
    "python_service_info", "Python platform information", ["current_version", "latest_version"]
)
nodejs_info = Gauge(
    "nodejs_service_info", "NodeJs platformm information", ["current_version", "latest_version"]
)


def update_metrics():
    docker = DockerService()
    elasticsearch = ElasticsearchService()
    kibana = KibanaService()
    java = JavaService()
    python = PythonService()
    nodejs = NodeJsService()

    docker_service_info.labels(
        current_version=docker.get_current_version(),
        latest_version=docker.get_latest_version(),
    )


if __name__ == "__main__":
    start_http_server(8000)
    while True:
        update_metrics()
        time.sleep(30)
