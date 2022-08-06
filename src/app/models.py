import sqlalchemy as sqla

from .db import Base


class QuizItem(Base):
    __tablename__ = "quiz_item"
    __mapper_args__ = {
        "eager_defaults": True
    }

    id = sqla.Column(sqla.Integer, primary_key=True)
    question = sqla.Column(sqla.String(512), nullable=False, index=True)
    answer = sqla.Column(sqla.String(512), nullable=False)
    created_at = sqla.Column(sqla.TIMESTAMP, nullable=False)

    saved_at = sqla.Column(sqla.TIMESTAMP, nullable=True, server_default=sqla.func.now(), index=True)

    def __repr__(self):
        return f"QuizItem. id: {self.id}, question: {self.question}, answer: {self.answer}," \
               f" created_at: {self.created_at}"
