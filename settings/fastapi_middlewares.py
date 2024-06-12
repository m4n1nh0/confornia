"""Fastapi app middleware."""

from fastapi import FastAPI, Request, status
from starlette.responses import JSONResponse
import time

from settings.infra_environment import InfraParameters


def fastapi_middleware(app: FastAPI):
    """Start events before uploading the system."""
    @app.middleware("http")
    async def verify_host(request: Request, call_next):
        """Request to prevent Host Header Injection."""
        ALLOWED_HOST = InfraParameters.ALLOWED_HOST
        start_time = time.time()
        if 'user-agent' in request.headers:
            if 'kube-probe' not in request.headers['user-agent']:
                if request.headers['Host'] not in ALLOWED_HOST \
                        or 'X-Forwarded-Host' in request.headers:
                    return JSONResponse(
                        content={'detail': 'Não autorizado.'},
                        status_code=status.HTTP_401_UNAUTHORIZED
                    )

        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
