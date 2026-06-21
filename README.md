````markdown
# API для Yatube

API для социальной сети Yatube. Позволяет публиковать посты, оставлять комментарии, подписываться на авторов.

## Установка

1. Клонировать репозиторий:
   ```bash
   git clone <url>
   cd api-final-yatube
   ```
````

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполнить миграции:

   ```bash
   cd yatube_api
   python manage.py migrate
   ```

5. Запустить сервер:
   ```bash
   python manage.py runserver
   ```

## Примеры запросов

### Получить список постов

```http
GET /api/v1/posts/
```

### Создать пост

```http
POST /api/v1/posts/
Content-Type: application/json
Authorization: Bearer <token>

{
    "text": "Текст поста"
}
```

### Подписаться на пользователя

```http
POST /api/v1/follow/
Content-Type: application/json
Authorization: Bearer <token>

{
    "following": "username"
}
```

## Документация

После запуска сервера документация доступна по адресу:

- http://127.0.0.1:8000/redoc/

```

```
