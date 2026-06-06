from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

DATABASE_URL = settings.DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://"
).split("?")[0]

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"ssl": "require"}  # asyncpg's way of requiring SSL
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

import app.models  