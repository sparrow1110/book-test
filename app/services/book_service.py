from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate
from app.utils.date_formatter import format_text_date


def create_book(
    db: Session,
    book_data: BookCreate
):
    book = Book(
        title=book_data.title,
        description=book_data.description,
        created_at=format_text_date()
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def get_all_books(db: Session):
    return db.query(Book).order_by(Book.id).all()