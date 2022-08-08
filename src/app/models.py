import sqlalchemy as sqla

from .db import Base


class QuizItem(Base):
    __tablename__ = "quiz_item"

    id = sqla.Column(sqla.Integer, primary_key=True)
    question = sqla.Column(sqla.String(512), nullable=False, index=True)
    answer = sqla.Column(sqla.String(512), nullable=False)
    created_at = sqla.Column(sqla.DateTime(timezone=True), nullable=False)

    def __repr__(self):
        return f"QuizItem. id: {self.id}, question: {self.question}, answer: {self.answer}," \
               f" created_at: {self.created_at}"
