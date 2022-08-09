import pytest
from httpx import AsyncClient
from fastapi import status

from app.db import get_db
from app.conftest import overrides_get_db
from app.main import app


@pytest.mark.asyncio
async def test_override_dependency():
    app.dependency_overrides[get_db] = overrides_get_db


@pytest.mark.asyncio
async def test_get_something(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/quiz",
        json={
            "count": 10
        }
    )

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_teardown_overrides():
    app.dependency_overrides = {}
