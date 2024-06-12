from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings.fastapi_middlewares import fastapi_middleware
from settings.infra_environment import FastApiIni
from settings.openapi import bas_openapi


def fastapi_app():
    __fastapi_app = FastAPI(
        docs_url=FastApiIni.docs_url,
        redoc_url=FastApiIni.redoc_url,
        openapi_url=FastApiIni.openapi_url
    )

    __fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    __fastapi_app.openapi = bas_openapi(__fastapi_app)

    fastapi_middleware(__fastapi_app)

    api = "/api"
    from routes import (questions, auditoria)

    __fastapi_app.include_router(questions.routes, prefix=api)
    __fastapi_app.include_router(auditoria.routes, prefix=api)

    return __fastapi_app
