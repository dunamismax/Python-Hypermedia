"""
Application configuration settings.

This module uses pydantic-settings to manage configuration.
Settings are loaded from environment variables, and a .env file is supported for local development.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Main application settings.
    """

    # Database URL for connecting to PostgreSQL.
    # The default value is suitable for local development.
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost/todo_app"

    # Configuration for loading settings from a .env file.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Create a single instance of the settings to be used throughout the application.
settings = Settings()
