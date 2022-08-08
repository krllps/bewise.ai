from fastapi import HTTPException, status
from pydantic import ValidationError

import httpx
from httpx import Response as HTTPXResponse, HTTPError as HTTPXError, ConnectError as HTTPXConnectError

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert  # allows using Postgres specific ON CONFLICT DO NOTHING construct

from typing import Any
import logging

from .config import settings
from .schemas import JServiceAPIResponse
from .models import QuizItem
from .db import AsyncSession

logging.basicConfig(level=logging.DEBUG)


def throw_http_503(detail: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail=detail
    )


async def fetch_quiz_items(n: int) -> list[dict[str, Any]]:
    """
    Makes an external API call and fetches n items

    :param n: n items to fetch (max 100 at a time)
    :returns: Fetched items
    :raises HTTP 503 SERVICE UNAVAILABLE, when fails to connect or timed out
    """
    url: str = f"https://jservice.io/api/random?count={n}"
    async with httpx.AsyncClient(
            timeout=settings.HTTPX_TIMEOUT,
            limits=settings.HTTPX_LIMITS
    ) as async_client:
        try:
            response: HTTPXResponse = await async_client.get(url=url)
            assert response.status_code == 200
            logging.info(msg=f"Fetched {n} data entries from jservice.io")
            return response.json()
        except AssertionError:
            logging.error(msg="Status code of requested resource is not 200")
            throw_http_503(detail="Failed to connect to jservice.io resource")
        except HTTPXError:
            logging.error(msg="Connection to jservice.io failed")
            throw_http_503(detail="Failed to connect to jservice.io resource")
        finally:
            await async_client.aclose()


def validate_item(item: dict[str, Any]) -> JServiceAPIResponse:
    try:
        return JServiceAPIResponse(**item)
    except ValidationError:
        logging.warning(msg=f"Failed to validate {item}")


def validate_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [validate_item(item).__dict__ for item in items]


async def insert_quiz_items(n: int, db: AsyncSession) -> None:
    """
    *Background task*: Fetches and inserts quiz items up until n is reached or fails to connect to jservice.io

    :param n: n items to insert
    :param db: Async transaction
    :return: null
    """
    n_inserted: int = 0
    while not n_inserted == n:
        n_rows_to_insert: int = n - n_inserted
        try:
            fetched_items: list[dict[str, Any]] = await fetch_quiz_items(n=n_rows_to_insert)
        except HTTPException:
            logging.error(msg="Failed to fetch data from jservice.io")
            break
        validated: list[dict[str, Any]] = validate_items(items=fetched_items)

        query = (
            insert(QuizItem).
            values(validated).
            on_conflict_do_nothing().
            returning()
        )

        result = await db.execute(query)
        n_inserted += result.rowcount
    if n_inserted == n:
        logging.info(msg="Success")


async def select_all(db: AsyncSession) -> list[QuizItem | None]:
    result = await db.execute(select(QuizItem))
    return result.scalars().all()
