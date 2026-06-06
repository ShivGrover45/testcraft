import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Integer, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.enums import Difficulty

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )
    domain_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("domains.id"))
    created_by: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    question_text: Mapped[str] = mapped_column(Text)
    options: Mapped[list] = mapped_column(JSONB)
    correct_answer: Mapped[int] = mapped_column(Integer)
    difficulty: Mapped[Difficulty] = mapped_column(
        SQLEnum(Difficulty), 
        default=Difficulty.medium
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    domain: Mapped["Domain"] = relationship("Domain", back_populates="questions")
    creator: Mapped["User"] = relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_questions"
    )
    test_questions: Mapped[List["TestQuestion"]] = relationship(
        "TestQuestion",
        back_populates="question",
        cascade="all, delete-orphan"
    )
    attempt_answers: Mapped[List["AttemptAnswer"]] = relationship(
        "AttemptAnswer",
        back_populates="question"
    )