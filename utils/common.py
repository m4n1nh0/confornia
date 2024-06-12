from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from db.postgres import SessionLocal as postgres_async


class Util:

    def __init__(self, session=None):
        self.session = session

    async def database_commit(self, model) -> SQLAlchemyError:
        """Generalized commit for used in the system."""
        try:
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
        except SQLAlchemyError as err:
            await self.session.rollback()
            return err

    @staticmethod
    def http_exception(message, status, headers=None) -> HTTPException:
        """Error message."""
        return HTTPException(
            status_code=status,
            detail=message,
            headers=headers
        )

    @staticmethod
    async def delete_none(data):
        """Delete the json key with None value."""
        keys = []
        for k, v in data.items():
            if v is None:
                keys.append(k)

        for k in keys:
            del data[k]
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']


async def get_db_postgres():
    """Dependency function that yields db sessions."""
    async with postgres_async() as session:
        try:
            yield session
        finally:
            await session.close()
