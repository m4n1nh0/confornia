from typing import Optional

from pydantic import BaseModel


class Questions(BaseModel):
    """Questions update schema."""

    id: int
    iso_name: Optional[str] = None
    question: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    excluded: Optional[bool] = False


class InsertQuestions(BaseModel):
    """Questions insert schema."""

    iso_name: str
    question: str
    description: str
    reference: Optional[str] = None
    excluded: Optional[bool] = False


class DeleteQuestions(BaseModel):
    """Questions delete schema."""

    id: int
