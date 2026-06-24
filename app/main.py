from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routers.books import router

app = FastAPI(
    title="Book API",
    description="REST API для работы с коллекцией книг",
    version="1.0.0"
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={
            "detail": exc.errors()
        }
    )


app.include_router(router)