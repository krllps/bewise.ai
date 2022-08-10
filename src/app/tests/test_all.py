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
async def test_call_for_quiz_items(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/quiz",
        json={"count": 10}
    )
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data == []


@pytest.mark.asyncio
async def test_call_for_quiz_items_null_count(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/quiz",
        json={"count": None}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_call_for_quiz_items_no_body(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/quiz"
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_call_for_quiz_items_invalid_count(async_client: AsyncClient) -> None:
    response = await async_client.post(
        url="/quiz",
        json={"count": 0}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    another_response = await async_client.post(
        url="/quiz",
        json={"count": 101}
    )
    assert another_response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_get_quiz_items(async_client: AsyncClient) -> None:
    response = await async_client.get(url="/quiz/items")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.asyncio
async def test_get_items_count(async_client: AsyncClient) -> None:
    response = await async_client.get(url="/quiz/items/count")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data.get("count") == 0


@pytest.mark.asyncio
async def test_teardown_overrides():
    app.dependency_overrides = {}
