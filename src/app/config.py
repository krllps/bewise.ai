from functools import lru_cache
import os


class BaseConfig:
    ...


class DevelopmentConfig(BaseConfig):
    PG_USER: str = os.environ.get("POSTGRES_USER")
    PG_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    PG_DB: str = os.environ.get("POSTGRES_DB")
    PG_HOST: str = os.environ.get("POSTGRES_HOST")

    PG_DB_URL: str = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DB}"


class ProductionConfig(BaseConfig):
    ...


class TestingConfig(BaseConfig):
    ...


@lru_cache()
def get_settings() -> object:
    """ Get app settings """
    configs: dict[str, object] = {
        "dev": DevelopmentConfig,
        "prod": ProductionConfig,
        "test": TestingConfig
    }

    stage: str = os.environ.get("STAGE", "dev")

    config: object = configs.get(stage) if stage in configs else configs.get("dev")
    return config


settings = get_settings()
