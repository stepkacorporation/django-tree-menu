# django-tree-menu

### Описание
Это Django приложение, представляющее собой систему управления меню. Оно позволяет создавать и управлять многоуровневыми меню для веб-сайта через админ-панель Django.

### Установка
#### Для Windows
```
git clone https://github.com/stepkacorporation/django-tree-menu.git
cd django-tree-menu
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd app
python manage.py migrate
```
#### Для Linux
```
git clone https://github.com/stepkacorporation/django-tree-menu.git
cd django-tree-menu
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd app
python manage.py migrate
```

### Использование
Меню можно отрисовать с помощью следующих шаблонных тегов:
```
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

### Загрузка тестовых данных
Если вам нужны тестовые данные, вы можете загрузить их с помощью команды:

#### Для Windows
```
python manage.py loaddata initial_data.json
```
#### Для Linux
```
python3 manage.py loaddata initial_data.json
```

### Создание суперпользователя и запуск сервера
#### Для Windows
```
python manage.py createsuperuser
python manage.py runserver
```
#### Для Linux
```
python3 manage.py createsuperuser
python3 manage.py runserver
```
