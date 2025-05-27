# Stripe Django Проект

Этот проект реализует простой интерфейс оплаты товаров через **Stripe Checkout**, используя **Django + PostgreSQL + Docker + Nginx**.

## 🧩 Функционал

- Отображение товара на HTML-странице
- Кнопка "Buy" → вызывает Stripe Checkout
- Редирект на страницу успеха или отмены
- Админка Django для управления товарами
- Полностью запускается через Docker и доступен на сервере

## 🛠️ Технологии

- **Python 3.11**
- **Django**
- **Stripe API**
- **PostgreSQL**
- **Gunicorn**
- **Nginx**
- **Docker & Docker Compose**

*🚀 Как запустить локально*

- Клонируйте репозиторий
```
git clone https://github.com/konfuzer/stripe_app.git
```

- Создайте `.env` файл в корне проекта:

```
env
# Django
SECRET_KEY='django-insecure-your-secret-key-here'
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# База данных
POSTGRES_DB=stripe_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5433

# Stripe ключи
STRIPE_SECRET_KEY_1=sk_test_...
STRIPE_PUBLISHABLE_KEY_1=pk_test_...
CURRENCY_1=USD

#опционально
STRIPE_SECRET_KEY_2=sk_test_...
STRIPE_PUBLISHABLE_KEY_2=pk_test_...
CURRENCY_2=EUR

# URL для редиректа
SUCCESS_URL=http://109.172.101.2:8080/success/
CANCEL_URL=http://109.172.101.2:8080/cancel/
```

- Перейдите в корневую папку проекта

```
cd stripe_app
```

- Убедитесь в том, что на вашем ПК запущен Docker

- Установите виртуальное окружение, зависимости

```
python -m venv venv
source venv/Scripts/activate (для bash)

pip install -r requirements.txt
```

- Соберите и запустите контейнеры

```
docker-compose up -d --build
```

- Войдите в контейнер бэкенда

```
docker exec -it stripe_app-backend-1 bash
```

- Примените миграции, соберите статику, создайте админа

```
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic

python manage.py createsuperuser
```

- Откройте сайт

Откройте в браузере:

http://127.0.0.1:8080/item/1

Перейдите в Админку:

http://127.0.0.1:8080/admin

## 🧪 Доступные маршруты

- /item/<id>

Показывает товар и кнопку Buy

- /buy/<id>

Создаёт Stripe Checkout Session

- /success/

Страница успешной оплаты

- /cancel/

Страница отмены оплаты

## 🛜 Доступность в интернете

Проект доступен на удаленном сервере по адресу 

http://109.172.101.2:8080/admin

http://109.172.101.2:8080/item/<id>