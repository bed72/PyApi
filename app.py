from fastapi import FastAPI

from src.presentation.routes import authentication_route

app = FastAPI(
    version="1.0.0",
    title="King's Cross",
    description="BFF Application",
)

app.include_router(prefix="/v1", router=authentication_route.router)
