import asyncio
from typing import Generator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings
from app.models import Base
from app.main import app, get_db

test_settings = get_settings(stage="test")

async_engine: AsyncEngine = create_async_engine(
    test_settings.PG_DB_URL,
    # echo=True,  # flash SQL queries
    future=True  # enable DBAPI 2.0
)


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def overrides_get_db() -> AsyncSession:
    session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with session() as async_session:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield async_session
        await async_session.commit()

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await async_engine.dispose()


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(app=app, base_url=f"http://localhost:8000/") as client:
        yield client
