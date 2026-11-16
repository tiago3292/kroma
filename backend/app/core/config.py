from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = Field(default=..., alias="DATABASE_URL")
    gemini_api_key: str = Field(default=..., alias="GEMINI_API_KEY")

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        populate_by_name=True,
    )

settings = Settings()