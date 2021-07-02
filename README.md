[![polls workflow](https://github.com/ps-iria/polls/actions/workflows/main.yml/badge.svg)](https://github.com/ps-iria/polls/actions/workflows/main.yml)
# Polls API
API для системы опросов пользователей

## Функционал для администратора системы

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

## Функционал для пользователей системы

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

### Запуск

- Создайте папку для проекта  `mkdir polls` и перейдите в нее `cd polls`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/ps-iria/polls .`
- Запустите docker-compose `sudo docker-compose up -d`
- Примените миграции `sudo docker-compose exec web python manage.py migrate`
- Соберите статику `sudo docker-compose exec web python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec web python manage.py createsuperuser`


## **Технологии**
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Gunicorn](https://gunicorn.org/)
- [Docker](https://www.docker.com/)