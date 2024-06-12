from typing import Optional

from pydantic import BaseModel


class Audit(BaseModel):
    """Audit update schema."""

    id: int
    name: Optional[str] = None
    audit_tipe: Optional[str] = None
    excluded: Optional[bool] = False
    empresa_id: Optional[int] = None


class InsertAudit(BaseModel):
    """Audit insert schema."""

    name: Optional[str] = None
    audit_tipe: Optional[str] = None
    excluded: Optional[bool] = False
    empresa_id: Optional[int] = None


class DeleteAudit(BaseModel):
    """Audit delete schema."""

    id: int
