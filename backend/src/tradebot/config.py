from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).parent.parent.parent.parent / ".env"


class Settings(BaseSettings):
    alpaca_api_key: SecretStr
    alpaca_secret_key: SecretStr
    alpaca_paper: bool

    model_config = SettingsConfigDict(env_file=ENV_FILE)


def get_settings() -> Settings:
    return Settings()
