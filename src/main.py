from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .core.config import APP_CONFIGS, get_settings
from .routers.api import api_router

app = FastAPI(**APP_CONFIGS)

settings = get_settings()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
