from application.book_service import BookService
from app.infra_storage.mem_storage import MemoryStorage
from app.infra_storage.sqlite_storage import SQLiteStorage


class Context:
    def __init__(self):
        book_storage = SQLiteStorage("test.db")
        self.book_service = BookService(book_storage)


def get_context(app):
    return app.config["CONTEXT"]