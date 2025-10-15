from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class ENV(BaseSettings):
    """Переменные окружения для запуска приложения"""
    POSTGRES_DSN: PostgresDsn
    """DSN для подключения к БД"""

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        validate_default=True,
        use_attribute_docstrings=True,
        env_file="../.env",
    )


class TEST_ENV(BaseSettings):
    """Переменные окружения для запуска тестов"""

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        validate_default=True,
        use_attribute_docstrings=True,
        env_file="../.env",
    )
