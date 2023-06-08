from fastapi import FastAPI

from config.config import APP_CONFIGS, get_settings

app = FastAPI(**APP_CONFIGS)

settings = get_settings()
