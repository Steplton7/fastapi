from typing import List
from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author

app = FastAPI()


@app.get('/')
def home():
    return {"key":"Hello"}


@app.get('/test/{pk}') # 127.0.0.1:8000/2?q=re
def get_item(pk: int, q: str = None):
    """ Пример работы url. """
    return {"key": pk, "q": q}


@app.get('user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    """ Пример работы url. """
    return {"user": pk, "item": item}



@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    """ Модели. Указание аргументов которые входят только в тело запроса, а не url."""
    return {"item": item, "author": author, "quantity": quantity}


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    """ Для того что бы в json был ключ Author."""
    return {"author": author}


@app.get('/book') # ... показывает что параметр обязательный
def gte_book(q: List[str] = Query(["1","2"], description='Search book')):
    """ Парметры."""
    return q


@app.get('/book/{pk}') # gt -min. le - max.
def get_single(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    """ Функция получения книги по id."""
    return {"pk": pk}