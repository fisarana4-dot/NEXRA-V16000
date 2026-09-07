import os

class Config:
    APP_NAME = os.getenv("APP_NAME", "NEXRA_V16000")
    DB_PATH = os.getenv("DB_PATH", "nexra_v16000.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    SECRET_KEY=os.getenv("SECRET_KEY","nexra-dev-secret")
    TRADINGVIEW_WEBHOOK_SECRET = os.getenv("TRADINGVIEW_WEBHOOK_SECRET")
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    DATABASE_URL=os.getenv("DATABASE_URL","sqlite+aiosqlite:///./nexra_v16000.db")
    REDIS_URL=os.getenv("REDIS_URL","redis://localhost:6379/0")


settings = Config()
