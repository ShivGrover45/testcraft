import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database import Base

class Domain(Base):
    __tablename__ = "domains"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, 
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_by: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    creator: Mapped["User"] = relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_domains"
    )
    experts: Mapped[List["User"]] = relationship(
        "User",
        foreign_keys="[User.domain_id]",
        back_populates="domain"
    )
    questions: Mapped[List["Question"]] = relationship(
        "Question", 
        back_populates="domain"
    )
    tests: Mapped[List["Test"]] = relationship(
        "Test", 
        back_populates="domain"
    )