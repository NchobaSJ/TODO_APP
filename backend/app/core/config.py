from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    SECRET: str = "CHANGE_ME_IN_PRODUCTION"
    DATABASE_URL: str = "sqlite+aiosqlite:///./todo.db"
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 3600

settings = Settings()