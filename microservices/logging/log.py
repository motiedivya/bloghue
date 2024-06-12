import logging
import requests
from .config import settings

logger = logging.getLogger("microservice_logger")
logger.setLevel(logging.INFO)

class ElasticsearchHandler(logging.Handler):
    def __init__(self, url, index):
        logging.Handler.__init__(self)
        self.url = url
        self.index = index

    def emit(self, record):
        log_entry = self.format(record)
        response = requests.post(f"{self.url}/{self.index}/_doc", json=log_entry)
        response.raise_for_status()

def init_logger():
    handler = ElasticsearchHandler(settings.elasticsearch_url, settings.index_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
