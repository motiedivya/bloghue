from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    secret_key: str = os.getenv("SECRET_KEY", "default_secret_key")

settings = Settings()
