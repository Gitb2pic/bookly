from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo=True
))


async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        from src.books.model import Book
        await conn.run_sync(SQLModel.metadata.create_all)
    