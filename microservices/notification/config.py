from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "your_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    smtp_server: str = "smtp.example.com"
    smtp_port: int = 587
    smtp_username: str = "your_email@example.com"
    smtp_password: str = "your_email_password"
    from_email: str = "your_email@example.com"

settings = Settings()
