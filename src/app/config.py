from functools import lru_cache
from httpx import Timeout, Limits
from typing import Literal
import os


class BaseConfig:
    ...


class DevelopmentConfig(BaseConfig):
    PG_USER: str = os.environ.get("POSTGRES_USER")
    PG_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    PG_DB: str = os.environ.get("POSTGRES_DB")
    PG_HOST: str = os.environ.get("POSTGRES_HOST")

    PG_DB_URL: str = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DB}"

    HTTPX_TIMEOUT: Timeout = Timeout(timeout=10)
    HTTPX_LIMITS: Limits = Limits(max_connections=50, max_keepalive_connections=25)


class ProductionConfig(BaseConfig):
    ...


class TestingConfig(BaseConfig):
    PG_USER: str = os.environ.get("POSTGRES_USER")
    PG_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    PG_DB: str = os.environ.get("TESTING_POSTGRES_DB")
    PG_HOST: str = os.environ.get("POSTGRES_HOST")

    PG_DB_URL: str = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DB}"

    HTTPX_TIMEOUT: Timeout = Timeout(timeout=10)
    HTTPX_LIMITS: Limits = Limits(max_connections=50, max_keepalive_connections=25)


@lru_cache()
def get_settings(stage: Literal['dev', 'prod', 'test'] = 'dev') -> object:
    """ Get app settings """
    configs: dict[str, object] = {
        "dev": DevelopmentConfig,
        "prod": ProductionConfig,
        "test": TestingConfig
    }

    config: object = configs.get(stage) if stage in configs else configs.get("dev")
    return config


settings = get_settings()
