## Приложение для хранения книг на Flask и SQLAlchemy, Domain Driven Design
#### Запуск приложения
```
python bookstore.py
```

Добавлена возможность работы с бд SQLite.

urls:
- http://127.0.0.1:5000/books/  GET-запрос - список всех книг
- http://127.0.0.1:5000/books/  POST-запрос с телом, например 
{"title":"Название","description":"Описание","publish_year":2023,"pages_count":100,"created_at":"2024-01-01"} - создание книги
- http://127.0.0.1:5000/books/id/  DELETE-запрос - удаление книги с указанным id
