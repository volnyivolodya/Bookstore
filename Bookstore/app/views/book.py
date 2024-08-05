import dataclasses
import json

from flask import Blueprint, current_app, request

from app.context import get_context
from app.domain.book import Book

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)

    return json.dumps([dataclasses.asdict(b) for b in ctx.book_service.get()])


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)

    book = Book(**request.json)
    book_id = ctx.book_service.add(book)
    return {"id": book_id, "book": book}


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)

    return {}