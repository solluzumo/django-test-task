## О проекте

Сервис написан с использованием Python, DRF, HTML, JS

Понятие ДДС было заменено на транзакцию для облегчения контекста, поэтому в проекте представлена модель Transaction вместо DDS и соответствующие методы и связные сущности.

Сервис реализует стандартный CRUD для всех сущностей, позволяя создавать, удалять и редактировать транзакции, статутсы, типы, категории и подкатегории, а так же связи между ними. 

Была настроена админ-панель, в базе сохранен пользователь admin с паролем 12345

Интерфейс реализован на базе django templates с использованием js и bootstrap.

База данных - sqlite, она же представлена в репозитории.
## Требования

- Python 3.11
- Django 5.2.8
- Остальные зависимости указаны в `requirements.txt`

# Установка Python

Для Windows: установить с официального сайта https://www.python.org/downloads/release/python-3110/

Для Linux:
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev
```
## Инструкция по запуску
1. Клонируем репозиторий, переходим в папку
```
git clone https://github.com/solluzumo/django-test-task.git
cd django-test-task
```
2. Создаём и активируем виртуальное окружение

```
# Windows
python3.11 -m venv venv ИЛИ py -3.11 -m venv venv

venv\Scripts\activate
------------------------
# Linux/macOS

python3.11 -m venv venv
source venv/bin/activate
```
3. Устанавливаем зависимости
```
pip install -r requirements.txt
```
4. Создаём суперпользователя для доступа к админ-панеле(необязательно)
```
python manage.py createsuperuser
```
5. Запускаем проект
```
python manage.py runserver
```
6. Переходим в браузере по адресу:
```
http://127.0.0.1:8000/
```
