Проект: OSH-test

auth_service – сервис аутентификации (регистрация, авторизация пользователей)
estate_service – сервис управления недвижимостью (CRUD-операции для объектов недвижимости и комнат)
Оба сервиса используют FastAPI для создания REST API, SQLAlchemy для работы с базой данных и PostgreSQL в качестве СУБД. Проект контейнеризован с использованием Docker и Docker Compose.

Структура проекта

├── auth_service
│   ├── app
│   │   ├── api
│   │   │   ├── routers.py
│   │   │   └── schemas.py
│   │   ├── database
│   │   │   ├── database.py
│   │   │   ├── migrations
│   │   │   │   └── ... (файлы Alembic)
│   │   │   └── models.py
│   │   └── main.py
│   ├── Dockerfile
│   └── Readme.md
├── estate_service
│   ├── app
│   │   ├── api
│   │   │   ├── routers
│   │   │   │   ├── properties.py
│   │   │   │   └── rooms.py
│   │   │   └── schemas
│   │   │       ├── property_schemas.py
│   │   │       └── room_schemas.py
│   │   ├── database
│   │   │   ├── database.py
│   │   │   ├── migrations
│   │   │   │   └── ... (файлы Alembic)
│   │   │   └── models.py
│   │   ├── main.py
│   │   └── estate_service.log
│   ├── Dockerfile
│   └── Readme.md
├── docker-compose.yml
├── requirements.txt
└── Taskfile.yml
Предварительные требования
Docker и Docker Compose должны быть установлены на вашей машине.
В корне проекта должен находиться файл .env с необходимыми переменными окружения (например, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME_AUTH, DB_NAME_ESTATE).
Запуск проекта
Сборка и запуск контейнеров

Из корневой директории проекта выполните:

docker compose up --build
Доступ к сервисам

auth_service будет доступен по адресу: http://localhost:8001
estate_service будет доступен по адресу: http://localhost:8000
Описание сервисов
auth_service
Сервис аутентификации реализует API для регистрации и авторизации пользователей.
Использует PostgreSQL (контейнер auth_db) в качестве базы данных.

estate_service
Сервис управления недвижимостью предоставляет CRUD-операции для объектов недвижимости и комнат.
Использует PostgreSQL (контейнер estate_db) для хранения данных.

Технологии
FastAPI – создание REST API.
SQLAlchemy – ORM для работы с базой данных.
PostgreSQL – СУБД.
Docker и Docker Compose – контейнеризация и оркестрация сервисов.
Alembic – миграции базы данных.
Миграции базы данных
Миграционные файлы находятся в каталогах migrations каждого сервиса. Используйте Alembic для управления схемой базы данных.

Логи
Логи сервиса estate_service записываются в файл estate_service/estate_service.log.

Дополнительные команды

Остановка контейнеров:
docker compose down

Запуск контейнеров в фоновом режиме:
docker compose up -d --build

Для удобства можно использовать Taskfile, из которого можно запускаьт команды:
task <название команды>