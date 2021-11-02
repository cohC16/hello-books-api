from flask import jsonify
from flask.helpers import make_response

def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

def test_put_a_book(client, two_saved_books):
    from app.models.book import Book
    entry = {
        "title": "Third Book",
        "description": "It really is third",
    }
    response = client.post("/books", json = entry)
    book = Book.query.get(3)
    response_body = {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    

    assert response.status_code == 201
    assert response_body == {
        "id":3,
        "title": "Third Book",
        "description": "It really is third",
    }
    


