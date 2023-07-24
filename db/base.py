import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


DB_NAME = 'restaurant'
DB_USER = os.getenv('USER_FOR_YLAB_DB')
DB_PASSWORD = os.getenv('PASSWORD_FOR_YLAB_DB')
DB_HOST = 'localhost'
DB_PORT = '5432'

DATABASE_URI = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

async_engine = create_async_engine(DATABASE_URI, echo=True)


async def init_models():
    from models import Base
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Dependency
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


if __name__ == '__main__':
    import asyncio
    asyncio.run(init_models())
