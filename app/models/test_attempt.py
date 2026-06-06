import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Integer, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.enums import AttemptStatus

class TestAttempt(Base):
    __tablename__ = "test_attempts"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tests.id"))
    candidate_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    started_at: Mapped[datetime] = mapped_column(server_default=func.now())
    submitted_at: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    status: Mapped[AttemptStatus] = mapped_column(
        SQLEnum(AttemptStatus),
        default=AttemptStatus.in_progress
    )

    # Relationships
    test: Mapped["Test"] = relationship("Test", back_populates="attempts")
    candidate: Mapped["User"] = relationship("User", back_populates="test_attempts")
    answers: Mapped[List["AttemptAnswer"]] = relationship(
        "AttemptAnswer",
        back_populates="attempt",
        cascade="all, delete-orphan"
    )