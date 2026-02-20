from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application settings
    app_name: str = "Question Answering API"
    app_version: str = "1.0.0"
    env: str = "dev"

    # Model settings
    model_name: str = "distilbert-base-cased-distilled-squad"

    # Logging settings
    log_level: str = "INFO"

    # Sever settings
    port: int = 8000

    class Config:
        env_prefic = ""
        case_sensitive = False

settings = Settings()