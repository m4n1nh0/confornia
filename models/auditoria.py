"""MitigationQuestions model implementation."""

from sqlalchemy import Column, Integer, String, and_, Boolean, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.abstract import BaseModel
from settings.conf_logger import Log, TypeLog
from utils.common import Util


class Audit(BaseModel):
    """Audit model."""

    __tablename__ = 'audit'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    audit_tipe = Column(String, nullable=False, index=True)
    excluded = Column(Boolean, nullable=True, default=False)
    empresa_id = Column(Integer, nullable=False, index=True)


class AuditDTO:
    """Audit Data Transfer Object."""

    def __init__(self, session: AsyncSession):
        """Class initialization."""
        self.session = session
        self.util = Util(session)

    async def get_all(self) -> Audit or dict:
        """Get all in table."""
        query = select(Audit).where(Audit.excluded.is_(False))
        result = await self.session.execute(query)
        return result.scalars().unique().all()

    async def get_all_by_type(self,
                              audit_tipe: str) -> Audit or dict:
        """Get all in table filtering by type."""
        query = select(Audit).where(
            and_(Audit.audit_tipe == audit_tipe,
                 Audit.excluded.is_(False))
        )

        result = await self.session.execute(query)
        return result.scalars().unique().all()

    async def get_id(self, pk_id: int) -> Audit:
        """Get data from id."""
        query = select(Audit).where(
            and_(Audit.id == pk_id))

        result = (await self.session.execute(query)).scalars().first()

        return result

    async def insert(self, question: dict) -> Audit:
        questions = Audit(**question)

        await self.util.database_commit(questions)

        return questions

    async def update(self, question: dict,
                     pk_id: int) -> bool:
        """."""
        try:
            if "id" in question:
                del question["id"]
            await self.util.delete_none(question)
            query = update(Audit).where(and_(
                Audit.id == pk_id)).values(question)

            await self.session.execute(query)
            await self.session.commit()
            return True
        except Exception as error:
            msg = f'Ocorreu um erro no update de auditoria: {error} '
            Log(__name__).show_log(TypeLog.info.value, msg)
            return False

    async def delete(self, pk_id: int) -> None:
        """."""
        questions = dict(excluded=True)
        query = update(Audit).where(and_(
            Audit.id == pk_id)).values(questions)

        await self.session.execute(query)
        await self.session.commit()
