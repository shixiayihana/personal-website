from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from common.settings import load_settings
from web.routes import health, indices, valuations

settings = load_settings()
app = FastAPI(title="A股分位观测站 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(settings.cors_origins),
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api")
app.include_router(indices.router, prefix="/api")
app.include_router(valuations.router, prefix="/api")