from fastapi import FastAPI, Depends, BackgroundTasks, Response, status, Query
from pydantic import PositiveInt

import logging
from typing import Literal

from .swagger import responses, descriptions
from .schemas import JServiceAPIResponse, CountParameter, ItemsCount
from .models import QuizItem
from .db import AsyncSession, get_db
from . import utils

app = FastAPI(
    title="quizAPI",
    version="0.1.0",
    description=descriptions.quizAPI
)

logging.basicConfig(level=logging.DEBUG)


@app.post(
    path="/quiz",
    tags=["Quiz"],
    responses=responses.call_for_quiz_items,
    description=descriptions.call_for_quiz_items
)
async def call_for_quiz_items(
        background_tasks: BackgroundTasks,
        count: CountParameter,
        db: AsyncSession = Depends(get_db)
):
    items: list[QuizItem | None] = await utils.select_all(db=db)
    background_tasks.add_task(utils.insert_quiz_items, count.count, db)
    logging.info(f"Request for {count.count} quiz items has been scheduled")
    try:
        last_inserted = items[-1]
        return JServiceAPIResponse(**last_inserted.__dict__)
    except IndexError:
        logging.info(msg="There are no quiz items yet, returning empty list instead")
        return []


@app.get(
    path="/quiz/items",
    tags=["Quiz"],
    response_model=list[JServiceAPIResponse | None],
    responses=responses.get_quiz_items,
    description=descriptions.get_quiz_items
)
async def get_quiz_items(
        limit: int = Query(default=10, gt=0, le=1000),
        order_by: Literal["id", "question", "answer", "created_at"] = "id",
        order: Literal["asc", "desc"] = "asc",
        db: AsyncSession = Depends(get_db)
):
    items = await utils.select_with_constraints(db=db, limit=limit, order_by=order_by, order=order)
    if not items:
        logging.info(msg="There are no quiz items yet, returning HTTP_204_NO_CONTENT instead")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return items


@app.get(
    path="/quiz/items/count",
    tags=["Quiz"],
    response_model=ItemsCount,
    responses=responses.get_items_count,
    description=descriptions.get_items_count
)
async def get_items_count(db: AsyncSession = Depends(get_db)):
    count: int = await utils.get_items_count(db=db)
    return ItemsCount(count=count)
