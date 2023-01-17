# fastapi
основы FastAPI

### Описание
Изучение основ FastAPI
 
### Технологии
Python 
FastAPI 
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом main.py выполните команду:
```
uvicorn main:app --reload
```
- Для запуска на определенном порту (например 8080):
```
uvicorn main:app --reload --port 8080
```