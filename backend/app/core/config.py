from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key: str = Field(default=..., alias="GEMINI_API_KEY")
    hf_token: str = Field(default=..., alias="HF_TOKEN")

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        populate_by_name=True,
    )

settings = Settings()