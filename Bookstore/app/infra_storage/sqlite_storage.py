from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.domain.book import Book as book_dc
from app.infra_storage.models import Base, Book


class SQLiteStorage:
    """Класс для работы с бд sqlite"""

    def __init__(self, db_name: str):
        sqlite_db = f'sqlite:///{db_name}'  # строка подключения
        engine = create_engine(sqlite_db)  # создаем движок SqlAlchemy
        Base.metadata.create_all(engine)  # создаем таблицы
        Session = sessionmaker(bind=engine)  # создаем класс сессии
        self.session = Session()

    def add(self, book):
        """Добавляет книгу в бд"""
        new_book = Book(title=book.title,
                        description=book.description,
                        publish_year=book.publish_year,
                        pages_count=book.pages_count,
                        created_at=book.created_at
                        )
        self.session.add(new_book)
        self.session.commit()
        return new_book.id

    def delete(self, id):
        """Удаляет книгу из бд"""
        row = self.session.query(Book).get(id)
        if row:
            self.session.delete(row)
            self.session.commit()

    def get(self):
        """Возвращает список всех книг"""
        query = self.session.query(Book).all()
        result = []
        for row in query:
            book = book_dc(title=row.title,
                           description=row.description,
                           publish_year=row.publish_year,
                           pages_count=row.pages_count,
                           created_at=row.created_at
                           )
            result.append(book)
        return result