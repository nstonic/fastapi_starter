from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from env_settings import ENV

envs = ENV()


class Base(DeclarativeBase):
    pass


engine = create_async_engine(str(envs.POSTGRES_DSN))
async_db_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_db_session_maker() as session:
        yield session
