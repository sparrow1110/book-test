from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.book import BookCreate
from app.schemas.book import BookResponse
from app.services.book_service import create_book
from app.services.book_service import get_all_books

router = APIRouter(
    prefix="/api",
    tags=["Books"]
)


@router.post(
    "/book/add",
    response_model=BookResponse,
    status_code=201,
    summary="Создание новой книги",
    description="Создает новую книгу и сохраняет её в базе данных.",
    responses={
        201: {
            "description": "Книга успешно создана",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Название книги",
                        "description": "Описание книги",
                        "created_at": "24 июня 2026 года"
                    }
                }
            }
        },
        400: {
            "description": "Ошибка валидации",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "title"],
                                "msg": "String should have at most 255 characters",
                                "type": "string_too_long"
                            }
                        ]
                    }
                }
            }
        },
        422: {
            "description": "Стандартный ответ FastAPI. Фактические ошибки валидации возвращаются как 400 Bad Request."
        },
        500: {
            "description": "Внутренняя ошибка сервера",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal server error"
                    }
                }
            }
        }
    }
)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_book(db, book)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.get(
    "/books",
    response_model=List[BookResponse],
    summary="Получение списка книг",
    description="Возвращает список всех книг.",
    responses={
        200: {
            "description": "Список книг",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "title": "Название книги 1",
                            "description": "Описание книги 1",
                            "created_at": "23 июня 2026 года"
                        },
                        {
                            "id": 2,
                            "title": "Название книги 2",
                            "description": "Описание книги 2",
                            "created_at": "24 июня 2026 года"
                        }
                    ]
                }
            }
        },
        500: {
            "description": "Внутренняя ошибка сервера",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal server error"
                    }
                }
            }
        }
    }
)
def get_books(
    db: Session = Depends(get_db)
):
    try:
        return get_all_books(db)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )