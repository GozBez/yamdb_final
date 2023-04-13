# API_YAMDB
REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке.

## Описание

Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».

### Запуск проекта в контейнерах docker-compose:

Клонируем репозиторий и переходим в него в командной строке:
```bash
git clone git@github.com:GozBez/yamdb_final.git
```

Переходим в папку /infra_sp2/infra/ с файлом docker-compose.yaml:
```bash
cd infra
```

Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):
```bash
docker-compose up -d --build
```

Выполнить миграции, создание суперпользователя и сгененировать статику
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

Создать переменные окружения в каталоге yamdb_final/infra/ по файлу примеру .env.example:
```bash
SECRET_KEY='12345' # укажите секретняй ключ (установите свой)
# переменные для сервера баз данных
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Открыть в браузер:
```bash
http://localhost/admin/
```

Создание дампа bd выполнялось в каталоге yamdb_final/infra/ командой:
```bash
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Для восстановления необходимо узнать id контейнера с django и залить базу:
```bash
docker container ls -a
docker cp fixtures.json <CONTAINER ID>:/app
# Предварительно настроено имя в docker-compose можно указать или сразу так
docker cp fixtures.json api_yamdb_django:/app
docker-compose exec web python manage.py loaddata fixtures.json
```

Чтобы удалить дамп базы из контейнера:
```bash
docker exec -it <CONTAINER ID> bash
# или
docker exec -it api_yamdb_django bash
rm fixtures.json
exit
```

Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Запуск проекта в dev-режиме

Клонируем репозиторий и переходим в него в командной строке:
```bash
git clone git@github.com:GozBez/yamdb_final.git
```

Войти в рабочий каталог:
```bash
cd yamdb_final
```

Cоздать и активировать виртуальное окружение:
```bash
py -3.7 -m venv venv - Для windows
python -m venv env - Для linux
```
```bash
source env/bin/activate - Для linux
source venv/Scripts/activate - Для windows
```

Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r api_yamdb/requirements.txt
```

Выполнить миграции:
```bash
cd api_yamdb
python manage.py migrate
```

Запустить проект:
```bash
cd api_yamdb
python manage.py runserver
```

#### Автор

Dmitry Golubev
