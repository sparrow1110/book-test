# Book API

Тестовое задание Backend Developer.

REST API для работы с коллекцией книг, разработанное на FastAPI.

## Стек

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Swagger/OpenAPI

## Запуск

### Клонирование

```bash
git clone https://github.com/sparrow1110/book-test.git
cd book-test
```

### Запуск проекта

```bash
# 1. Создать .env файл
cp .env.example .env

docker-compose up --build
```
При запуске контейнера миграции Alembic применяются автоматически.

API будет доступно:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```


---

## Создание книги

POST

```
/api/book/add
```

Пример запроса:

```json
{
  "title": "Название книги",
  "description": "Описание книги"
}
```

Пример ответа:

```json
{
  "id": 1,
  "title": "Название книги",
  "description": "Описание книги",
  "created_at": "24 июня 2026 года"
}
```

---

## Получение списка книг

GET

```
/api/books
```

Пример ответа:

```json
[
  {
    "id": 1,
    "title": "Название книги",
    "description": "Описание книги",
    "created_at": "24 июня 2026 года"
  }
]
```
