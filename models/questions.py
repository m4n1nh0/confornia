"""MitigationQuestions model implementation."""

from sqlalchemy import Column, Integer, String, and_, Boolean, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.abstract import BaseModel
from settings.conf_logger import Log, TypeLog
from utils.common import Util


class Questions(BaseModel):
    """Questions model."""

    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    iso_name = Column(String, index=True)
    question = Column(String, nullable=False)
    description = Column(String, nullable=False)
    reference = Column(String, nullable=True)
    excluded = Column(Boolean, nullable=True, default=False)


class QuestionsDTO:
    """Questions Data Transfer Object."""

    def __init__(self, session: AsyncSession):
        """Class initialization."""
        self.session = session
        self.util = Util(session)

    async def get_all(self) -> Questions or dict:
        """Get all in table."""
        query = select(Questions).where(Questions.excluded.is_(False))
        result = await self.session.execute(query)
        return result.scalars().unique().all()

    async def get_all_by_type(self,
                              iso_name: str) -> Questions or dict:
        """Get all in table filtering by type."""
        query = select(Questions).where(
            and_(Questions.iso_name == iso_name,
                 Questions.excluded.is_(False))
        )

        result = await self.session.execute(query)
        return result.scalars().unique().all()

    async def get_id(self, pk_id: int) -> Questions:
        """Get data from id."""
        query = select(Questions).where(
            and_(Questions.id == pk_id))

        result = (await self.session.execute(query)).scalars().first()

        return result

    async def insert(self, question: dict) -> Questions:
        questions = Questions(**question)

        await self.util.database_commit(questions)

        return questions

    async def update(self, question: dict,
                     pk_id: int) -> bool:
        """."""
        try:
            if "id" in question:
                del question["id"]
            await self.util.delete_none(question)
            query = update(Questions).where(and_(
                Questions.id == pk_id)).values(question)

            await self.session.execute(query)
            await self.session.commit()
            return True
        except Exception as error:
            msg = f'Ocorreu um erro no update do adversário: {error} '
            Log(__name__).show_log(TypeLog.info.value, msg)
            return False

    async def delete(self, pk_id: int) -> None:
        """."""
        questions = dict(excluded=True)
        query = update(Questions).where(and_(
            Questions.id == pk_id)).values(questions)

        await self.session.execute(query)
        await self.session.commit()
