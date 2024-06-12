from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.auditoria import Audit, AuditDTO
from schema.auditoria import Audit as AuditSchema, InsertAudit
from settings.conf_logger import Log, TypeLog
from utils.common import get_db_postgres
from utils.responses.questions_responses import questions_responses

routes = APIRouter(tags=["Audit"],
                   prefix="/audit")


@routes.get("/v1/all",
            response_model=list[AuditSchema],
            responses=questions_responses.get("all"))
async def get_audits(
        session: AsyncSession = Depends(get_db_postgres)) -> list[AuditSchema]:
    """Get all audits data."""
    result = await AuditDTO(session).get_all()

    return result


@routes.get("/v1/{audit_id}",
            response_model=AuditSchema,
            responses=questions_responses.get("single"))
async def get_audit(
        audit_id: int,
        session: AsyncSession = Depends(get_db_postgres)) -> Audit:
    """Get a single audit."""

    audit = await AuditDTO(session).get_id(audit_id)

    msg = f'Auditor requisitada: {audit.nome}'
    Log(__name__).show_log(TypeLog.info.value, msg)

    return audit


@routes.post("/v1/register",
             response_model=AuditSchema,
             responses=questions_responses.get("update"))
async def audit_register(
        audit_data: InsertAudit,
        session: AsyncSession = Depends(get_db_postgres)):
    # Instantiating the audit class
    audit_dto = AuditDTO(session)
    # Converting to a audit.
    audit_data = audit_data.dict()
    # Inserting audit data.
    audit_db = await audit_dto.insert(audit_data)

    return {"detail": "Questão registrada.", "question": audit_db}


@routes.put("/v1/update/{audit_id}",
            response_model=AuditSchema,
            responses=questions_responses.get("update"))
async def update_audit(
        audit_id: int,
        audit_data: AuditSchema,
        session: AsyncSession = Depends(get_db_postgres)):
    # Instantiating the question class
    audit_dto = AuditDTO(session)
    audit_get = await audit_dto.get_id(audit_id)
    if audit_get is None:
        raise audit_dto.util.http_exception(
            message="Registro não encontrado.",
            status_code=404
        )
    # Converting to a question.
    audit_data = audit_data.dict()
    # Inserting question data.
    validation = await audit_dto.update(audit_data, audit_id)

    if validation:
        return {"detail": "Auditoria atualizada."}
    else:
        raise audit_dto.util.http_exception(
            message="Falha na atualização da questão",
            status_code=400
        )


@routes.delete("/v1/delete/{audit_id}",
               responses=questions_responses.get("delete"))
async def delete_audit(
        audit_id: int,
        session: AsyncSession = Depends(get_db_postgres)):

    audit_dto = AuditDTO(session)
    audit_get = await audit_dto.get_id(audit_id)
    if audit_get is None:
        raise audit_dto.util.http_exception(
            message="Registro não encontrado.",
            status_code=404
        )

    await audit_dto.delete(audit_id)
    return {"detail": "Auditoria deletada com sucesso",
            "question": audit_get}
