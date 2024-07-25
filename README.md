# django-tree-menu (Test Task)

## Описание

Это Django приложение, представляющее собой систему управления меню. Оно позволяет создавать и управлять многоуровневыми меню для веб-сайта через админ-панель Django.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/stepkacorporation/django-tree-menu.git
cd django-tree-menu
```

2. Запустите проект в контейнере Docker:

```bash
docker-compose up -d --build
```

3. Загрузите тестовые данные (если необходимо):

```bash
docker-compose exec web python manage.py loaddata initial_data.json
```

4. Создайте суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

## Использование

Меню можно отрисовать с помощью следующих шаблонных тегов:

```
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

## Просмотр примера работы меню

Если вы загрузили тестовые данные, пример работы меню можно просмотреть по следующему адресу: http://localhost:8000.  
Админ-панель: http://localhost:8000/admin.
