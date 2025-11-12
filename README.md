## Требования

- Python 3.11
- Django 5.2.8
- Остальные зависимости указаны в `requirements.txt`

## Инструкция по запуску
Клонируем репозиторий, переходим в папку
```
git clone https://github.com/solluzumo/django-test-task.git
cd django-test-task
```
Создаём и активируем виртуальное окружение
# Windows
```
python -m venv venv
venv\Scripts\activate
```
# Linux/macOS
```
python -m venv venv
source venv/bin/activate
```
Устанавливаем зависимости
```
pip install --upgrade pip
pip install -r requirements.txt
```
Создаём суперпользователя для доступа к админ-панеле(необязательно)
```
python manage.py createsuperuser
```
Запускаем проект
```
python manage.py runserver
```
Перейдите в браузере по адресу:
```
http://127.0.0.1:8000/
```
