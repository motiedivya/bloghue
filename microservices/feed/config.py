from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    post_service_url: str = "http://localhost:8002"

settings = Settings()
