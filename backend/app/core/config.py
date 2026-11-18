from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = Field(default=..., alias="DATABASE_URL")
    secret_key: str = Field(default=..., alias="SECRET_KEY")
    algorithm: str = Field(default=..., alias="ALGORITHM")
    access_token_expire_minutes: int = Field(default=..., alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    gemini_api_key: str = Field(default=..., alias="GEMINI_API_KEY")

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        populate_by_name=True,
    )

settings = Settings()