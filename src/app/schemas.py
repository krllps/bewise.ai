from pydantic import BaseModel, Field

from datetime import datetime


class JServiceAPIResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True


class CountParameter(BaseModel):
    count: int = Field(default=..., gt=0, le=100)


class ItemsCount(BaseModel):
    count: int
