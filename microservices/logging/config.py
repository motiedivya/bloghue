from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    elasticsearch_url: str = "http://localhost:9200"
    logstash_url: str = "http://localhost:5044"
    kibana_url: str = "http://localhost:5601"
    index_name: str = "microservice_logs"

settings = Settings()
