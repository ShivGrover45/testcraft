import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.enums import UserRole

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(254), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole), 
        default=UserRole.candidate
    )
    domain_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("domains.id", use_alter=True, name="fk_users_domain_id"),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    domain: Mapped[Optional["Domain"]] = relationship(
        "Domain",
        foreign_keys=[domain_id],
        back_populates="experts"
    )
    created_domains: Mapped[List["Domain"]] = relationship(
        "Domain",
        foreign_keys="[Domain.created_by]",
        back_populates="creator"
    )
    created_questions: Mapped[List["Question"]] = relationship(
        "Question",
        foreign_keys="[Question.created_by]",
        back_populates="creator"
    )
    created_tests: Mapped[List["Test"]] = relationship(
        "Test",
        foreign_keys="[Test.created_by]",
        back_populates="creator"
    )
    test_attempts: Mapped[List["TestAttempt"]] = relationship(
        "TestAttempt",
        back_populates="candidate"
    )