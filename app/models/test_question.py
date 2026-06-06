import uuid
from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.questions import Question
from app.models.test import Test

class TestQuestion(Base):
    __tablename__ = "test_questions"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tests.id"))
    question_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("questions.id"))
    marks: Mapped[int] = mapped_column(Integer, default=1)
    order_index: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (
        UniqueConstraint("test_id", "question_id", name="uq_test_question"),
    )

    # Relationships
    test: Mapped["Test"] = relationship("Test", back_populates="test_questions")
    question: Mapped["Question"] = relationship("Question", back_populates="test_questions")