## Требования

- Python 3.11
- Django 4.x (уточни конкретную версию из `requirements.txt`)
- Остальные зависимости указаны в `requirements.txt`

## Инструкция по запуску
Клонируем репозиторий
```
git clone https://github.com/solluzumo/django-test-task.git
```
Создаём и активируем виртуальное окружение
```
# Windows
python3.11 -m venv venv
venv\Scripts\activate

# Linux/macOS
python3.11 -m venv venv
source venv/bin/activate
```
Устанавливаем зависимости
```
pip install --upgrade pip
pip install -r requirements.txt
```
Создаём суперпользователя
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
