# Проект Atomic habits
Atomic Tracker - это приложение для отслеживания и управления своими привычками.

## Стек технологий
Проект разработан с использованием следующего технологического стека:

- Python 3.11
- Django: веб-фреймворк для создания веб-приложений
- Django REST framework: библиотека для создания RESTful API
- Celery: для асинхронных задач
- Redis: как брокер сообщений для Celery

## Установка и запуск проекта
Чтобы установить и запустить проект, выполните следующие шаги:

Клонируйте репозиторий:

```git clone git@github.com:VeraSamohina/Atomic_habits_DRF.git```

Установите зависимости

```pip install -r requirements.txt```

Создайте в корневой директории проекта файл .env и добавьте в него переменные среды, указанные в файле .env_sample

Выполните миграции для создания базы данных:

```python manage.py migrate```

 Запустите приложение:

```python manage.py runserver```

Запустите Celery для отправки уведомлений

```celery -A atomichabit worker -l info```

```celery -A atomichabit beat -S django```

## Документация проекта
Документация по эндпоинтам проекта находится по адресу

<http://127.0.0.1:8000/swagger/>

<http://127.0.0.1:8000/redoc/>