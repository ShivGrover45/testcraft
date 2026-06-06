from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

DATABASE_URL=settings.DATABASE_URL.replace("postgresql://","postgresql+asyncpg://")
engine=create_async_engine(DATABASE_URL,echo=True)
async_session_local=async_sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session_local() as session:
        try:
            yield session
        finally:
            await session.close()