from pathlib import Path

from prettyconf import config


class FastApiIni(object):
    docs_url = config("DOCS", default=None)
    redoc_url = config("REDOC", default=None)
    openapi_url = config("OPEN_API_URL", default=None)


class InfraParameters(object):
    POSTGRES_URL = config('POSTGRES_URL')
    ROOT_DIR = Path(__file__).parent.parent
    ALLOW_ORIGINS = config("ALLOW_ORIGINS", default=None)
    ALLOWED_HOST = config("ALLOWED_HOST", default=None)

    if ',' in ALLOWED_HOST:
        AMBIENT_HOST = ALLOWED_HOST.split(',')
    else:
        AMBIENT_HOST = [ALLOWED_HOST]

    if "," in ALLOW_ORIGINS:
        ALLOW_ORIGINS = ALLOW_ORIGINS.split(",")
    else:
        ALLOW_ORIGINS = [ALLOW_ORIGINS]

