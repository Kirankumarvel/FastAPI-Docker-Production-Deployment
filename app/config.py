import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Application settings
    APP_NAME: str = "FastAPI Docker Production"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Gunicorn settings
    WORKERS: int = int(os.getenv("WORKERS", "4"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    
    @property
    def is_production(self) -> bool:
        return not self.DEBUG

settings = Settings()