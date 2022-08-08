from fastapi import FastAPI, Depends, BackgroundTasks

import logging

from .schemas import JServiceAPIResponse, CountParameter
from .models import QuizItem
from .db import AsyncSession, get_db
from . import utils

app = FastAPI(
    title="quizAPI",
    version="0.1.0"
)

logging.basicConfig(level=logging.DEBUG)


@app.post(path="/quiz")
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
