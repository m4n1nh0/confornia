"""Postgresql database implementation."""

from prettyconf import config
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession,
                                    async_sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

postgres_url = config(
    "POSTGRES_URL",
    default="postgresql://postgres:postgres@localhost:5432/confornia")

async_engine = create_async_engine(postgres_url, poolclass=NullPool,
                                   future=True)

SessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


def news_connections(db_string: str):
    """Get new database connections from other microservices."""
    return create_async_engine(db_string, poolclass=NullPool, future=True)
