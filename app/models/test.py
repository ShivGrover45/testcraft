import uuid
from datetime import datetime
from typing import List
from sqlalchemy import String, Integer, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.enums import TestStatus

class Test(Base):
    __tablename__ = "tests"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(200))
    domain_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("domains.id"))
    created_by: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    duration_minutes: Mapped[int] = mapped_column(Integer)
    status: Mapped[TestStatus] = mapped_column(
        SQLEnum(TestStatus), 
        default=TestStatus.draft
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    domain: Mapped["Domain"] = relationship("Domain", back_populates="tests")
    creator: Mapped["User"] = relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_tests"
    )
    test_questions: Mapped[List["TestQuestion"]] = relationship(
        "TestQuestion",
        back_populates="test",
        cascade="all, delete-orphan"
    )
    attempts: Mapped[List["TestAttempt"]] = relationship(
        "TestAttempt",
        back_populates="test"
    )