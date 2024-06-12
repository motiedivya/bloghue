from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    nsq_lookupd_url: str = "http://localhost:4161"
    nsq_writer_url: str = "http://localhost:4150"
    topic_name: str = "microservice_topic"

settings = Settings()
