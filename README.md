# Foodgram, «Продуктовый помощник». Дипломный проект.
[![example workflow](https://github.com/south-punk/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/south-punk/foodgram-project-react/actions/workflows/main.yml)

[![Python](https://img.shields.io/badge/Python-blue?logo=Python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-blue?logo=GitHub&logoColor=white)](https://github.com/)
[![GitHub%20Actions](https://img.shields.io/badge/GitHub%20Actions-blue?logo=GitHub%20Actions&logoColor=white)](https://github.com/features/actions)
[![Django](https://img.shields.io/badge/Django-blue?logo=Django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?logo=PostgreSQL&logoColor=white)](https://www.postgresql.org/)
[![NGINX](https://img.shields.io/badge/NGINX-blue?logo=NGINX&logoColor=white)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/gunicorn-blue?logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=Docker&logoColor=white)](https://www.docker.com/)
[![Yandex.Cloud](https://img.shields.io/badge/Yandex.Cloud-blue?logo=Yandex.Cloud&logoColor=white)](https://cloud.yandex.ru/)

##  Описание
 Cайт Foodgram («Продуктовый помощник») - онлайн-сервис на котором можно публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
 
### Перед деплоем необходимо подготовить сервер. 
Для этого следует выполнить следующие шаги:
- **Остановить службу nginx:**
```bash
sudo systemctl stop nginx 
```
- **Установить docker:**
```bash
sudo apt install docker.io
```
- **Установить docker-compose:**
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)"-o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
- ***Скопировать файлы main.yaml и nginx.conf на сервер c локальной машины:**
перейти в директорию с файлом **docker-compose.yaml** и **nginx.conf** и выполнить команды:
```bash
scp docker-compose.yaml <username>@<host>:home/<username>/
scp nginx.conf <username>@<host>:home/<username>/
```
- **Добавить в Secrets GitHub Actions переменные окружения:**  
    - **DEBUG** - Вкл./выкл. режима отладки в настройках Django
    - **CORS_ALLOWED_ORIGINS** - список адресов, с которых разрешены запросы
    - **SECRET_KEY** - секретный ключ для файла настроек Django
    - **ALLOWED_HOSTS** - список доступных адресов проекта
    - **SSH_KEY** - ssh private key для доступа к удаленному серверу
    - **HOST** - id адрес хоста
    - **USER** - имя user-а на удаленном сервере
    - **PASSPHRASE** - пароль подтверждения подключения по ssh-key
    - **DOCKER_USERNAME** - username на DockerHub
    - **DOCKER_PASSWORD** - пароль на DockerHub
    - **POSTGRES_USER** - имя пользователя для базы данных
    - **POSTGRES_PASSWORD** - пароль для подключения к базе
    - **DB_ENGINE** - настойка подключения django-проекта к postgresql
    - **DB_NAME** - имя базы данных
    - **DB_HOST** - название сервиса (контейнера)
    - **DB_PORT** - порт для подключения к БД
    - **TELEGRAM_TOKEN** - token telegram-бота
    - **TELEGRAM_TO** - id пользователя, которому будут приходить оповещения об успешном деплои

### После деплоя необходимо 
- **Выполнить миграции:**
```bash
sudo docker-compose exec backend python manage.py makemigrations
```
- **Выполнить миграции:**
```bash
sudo docker-compose exec backend python manage.py migrate
```
- **Создать суперпользователя:**
```bash
sudo docker-compose exec backend python manage.py createsuperuser
```
- **Собрать статику:**
```bash
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
- **Наполнить базу данными:**
```bash
sudo docker-compose exec backend python manage.py loadtodb
```

**Сервис доступен по адресам**:  [51.250.97.178](http://51.250.97.178) или [bigfood.sytes.net](http://bigfood.sytes.net)  
**Документация API с примерами**: [51.250.97.178/api/docs/](http://51.250.97.178/api/docs/) или [bigfood.sytes.net/api/docs/](http://bigfood.sytes.net/api/docs/redoc.html)  
**Админ-панель**:  [51.250.97.178/admin](http://51.250.97.178/admin) или [bigfood.sytes.net/admin](http://bigfood.sytes.net/admin)  
**Login & password**: andy