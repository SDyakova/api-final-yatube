# API для Yatube

API для социальной сети Yatube. Позволяет публиковать посты, оставлять комментарии, подписываться на авторов и просматривать группы.

## Стек

- Python 3.12
- Django 5
- Django REST Framework
- Simple JWT
- SQLite

## Как развернуть проект

Клонировать репозиторий и перейти в папку:
git clone <url>
cd api-final-yatube

Создать виртуальное окружение и активировать:
python -m venv venv
source venv/Scripts/activate

Установить зависимости:
pip install -r requirements.txt

Выполнить миграции и запустить:
cd yatube_api
python manage.py migrate
python manage.py runserver

Документация API: http://127.0.0.1:8000/redoc/

## Возможности API

- Посты: просмотр, создание, редактирование, удаление
- Комментарии: просмотр, создание, редактирование, удаление
- Группы: только просмотр
- Подписки: свои подписки, подписка на автора
- JWT-аутентификация

Неавторизованные — только чтение. Авторизованные — создание, редактирование и удаление своего контента.

## Примеры запросов

### Получить токен

POST /api/v1/jwt/create/
Content-Type: application/json

{"username": "user", "password": "password"}

Ответ: {"refresh": "...", "access": "..."}

### Список постов

GET /api/v1/posts/

Ответ: [{"id": 1, "text": "Текст", "author": "user", ...}]

### Создать пост

POST /api/v1/posts/
Authorization: Bearer <токен>

{"text": "Новый пост"}

### Подписаться на автора

POST /api/v1/follow/
Authorization: Bearer <токен>

{"following": "author_username"}

Ответ: {"user": "user", "following": "author_username"}

## Автор

Дьякова Светлана Сергеевна
