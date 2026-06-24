from typing import Optional

from pydantic import BaseModel, field_validator
from pydantic import ConfigDict
from pydantic import Field


class BookCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Название книги",
        example="Название книги"
    )

    description: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="Описание книги",
        example="Описание книги"
    )

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError(
                "Title must not be empty"
            )

        return value


class BookResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 123,
                "title": "Название книги",
                "description": "Описание книги",
                "created_at": "23 июня 2026 года"
            }
        }
    )