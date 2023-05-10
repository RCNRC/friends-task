# friends-task

Этот репозиторий является решением задания первого этапа отбора в Vk на позицию стажёра. Представляет собой сервис, в котором участники могут регистрироваться, добавлять друг друга в друзья, просматривать список своих друзей и заявок в друзья.

## Установка

Требуется [Python](https://www.python.org/downloads/) версии 3.10 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip install --destination-directory DIR -r requirements.txt
```

В конце сгенерируёте секретный ключ `secret_key`, в котором будет не меньше 50 символов и не меньше 5 уникальных символов, создайте файл `.env` в корне проекта и поместите туда строку `DJANGO_SECRET_KEY=secret_key`.

## Запуск

1. В корне проекта выполните команду: `python3 manage.py migrate`.
2. В корне проекта выполните команду: `python3 manage.py runserver`. Сервер запустится на локальном сайте http://127.0.0.1:8000/

## OpenAPI документация

Полная документация по OpenAPI представлена в виде схемы [openapi-schema.yml](openapi-schema.yml).

### Часто используемые запросы

Далее все данные передаются в формате JSON.

1. Создание пользователя.
   - метод: `POST`
   - endpoint: `auth/users/`
   - тело запроса:
     - `username`: `имя создаваемого пользователя`
     - `password`: `пароль создаваемого пользователя`
2. Вход пользователя. В ответе будет лежать **токен `tok` для авторизации**, который требуется во всех остальных запросах класть в заголовок как `"Authorization": "Token tok"`
   - метод: `POST`
   - endpoint: `auth/token/login`
   - тело запроса:
     - `username`: `имя создаваемого пользователя`
     - `password`: `пароль создаваемого пользователя`
3. Отправка заявки в друзья пользователю с именем `name`.
   - метод: `POST`
   - endpoint: `api/v1/request/`
   - параметры запроса:
     - `username=name` - имя пользователя
   - требуется токен
4. Принятие заявки в друзья от пользователя с именем `name`.
   - метод: `POST`
   - endpoint: `api/v1/accept/`
   - параметры запроса:
     - `username=name` - имя пользователя
   - требуется токен
5. Отклонение заявки в друзья от пользователя с именем `name`.
   - метод: `POST`
   - endpoint: `api/v1/decline/`
   - параметры запроса:
     - `username=name` - имя пользователя
   - требуется токен
6. Удаление из друзей пользователя с именем `name`.
   - метод: `POST`
   - endpoint: `api/v1/remove/`
   - параметры запроса:
     - `username=name` - имя пользователя
   - требуется токен
7. Получение всех исходящих и входящих запросов.
   - метод: `GET`
   - endpoint: `api/v1/requests/`
   - требуется токен
8. Получение всех друзей.
   - метод: `GET`
   - endpoint: `api/v1/friendships/`
   - требуется токен
9. Получение статуса отношений с пользователем с именем `name`.
   - метод: `GET`
   - endpoint: `api/v1/status/`
   - параметры запроса:
     - `username=name` - имя пользователя
   - требуется токен
