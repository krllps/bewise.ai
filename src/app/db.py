from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

from fastapi import HTTPException
from typing import AsyncGenerator

from .config import settings

async_engine: AsyncEngine = create_async_engine(
    settings.PG_DB_URL,
    # echo=True,  # flash SQL queries
    future=True  # enable DBAPI 2.0
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    async with AsyncSession(bind=async_engine, expire_on_commit=False, future=True) as async_session:
        try:
            yield async_session
            await async_session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            await async_session.rollback()
            raise sqlalchemy_error
        except HTTPException as http_exception:
            await async_session.rollback()
            raise http_exception
        finally:
            await async_session.close()
