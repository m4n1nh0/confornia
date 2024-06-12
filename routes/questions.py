from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.questions import Questions, QuestionsDTO
from schema.questions import Questions as QuestionSchema, InsertQuestions
from settings.conf_logger import Log, TypeLog
from utils.common import get_db_postgres, Util
from utils.responses.questions_responses import questions_responses

routes = APIRouter(tags=["Questions"],
                   prefix="/questions")


@routes.get("/v1/all",
            response_model=list[QuestionSchema],
            responses=questions_responses.get("all"))
async def get_questions(
        session: AsyncSession = Depends(get_db_postgres)) -> list[QuestionSchema]:
    """Get all questions data."""
    result = await QuestionsDTO(session).get_all()

    return result


@routes.get("/v1/{question_id}",
            response_model=QuestionSchema,
            responses=questions_responses.get("single"))
async def get_question(
        question_id: int,
        session: AsyncSession = Depends(get_db_postgres)) -> Questions:
    """Get a single adversary."""

    question = await QuestionsDTO(session).get_id(question_id)

    msg = f'Questão requisitada: {question.description}'
    Log(__name__).show_log(TypeLog.info.value, msg)

    return question


@routes.post("/v1/register",
             response_model=QuestionSchema,
             responses=questions_responses.get("update"))
async def question_register(
        question: InsertQuestions,
        session: AsyncSession = Depends(get_db_postgres)):
    # Instantiating the question class
    question_dto = QuestionsDTO(session)
    # Converting to a question.
    question_data = question.dict()
    # Inserting question data.
    question_db = await question_dto.insert(question_data)

    return {"detail": "Questão registrada.", "question": question_db}


@routes.put("/v1/update/{question_id}",
            response_model=QuestionSchema,
            responses=questions_responses.get("update"))
async def update_question(
        question_id: int,
        question: QuestionSchema,
        session: AsyncSession = Depends(get_db_postgres)):
    # Instantiating the question class
    question_dto = QuestionsDTO(session)
    question_get = await QuestionsDTO(session).get_id(question_id)
    if question_get is None:
        raise question_dto.util.http_exception(
            message="Registro não encontrado.",
            status_code=404
        )
    # Converting to a question.
    question_data = question.dict()
    # Inserting question data.
    validation = await question_dto.update(question_data, question_id)

    if validation:
        return {"detail": "Questão atualizada."}
    else:
        raise question_dto.util.http_exception(
            message="Falha na atualização da questão",
            status_code=400
        )


@routes.delete("/v1/delete/{question_id}",
               responses=questions_responses.get("delete"))
async def delete_question(
        question_id: int,
        session: AsyncSession = Depends(get_db_postgres)):

    question_dto = QuestionsDTO(session)
    question = await QuestionsDTO(session).get_id(question_id)
    if question is None:
        raise question_dto.util.http_exception(
            message="Registro não encontrado.",
            status_code=404
        )

    await question_dto.delete(question_id)
    return {"detail": "Questão deletada com sucesso",
            "question": question}
