# "REST API для меню ресторана"

Этот проект представляет собой REST API для управления меню ресторана с использованием FastAPI и PostgreSQL в качестве базы данных.

## Зависимости

Для работы проекта необходимо установить следующие зависимости:

*    Python 3.x
*    PostgreSQL (создать базу данных)

Для установки Python-зависимостей, выполните следующую команду:

```pip install -r requirements.txt```

## Настройка базы данных

Для настройки базы данных, выполните следующие шаги:

* Создайте базу данных PostgreSQL, указав соответствующие параметры в файле db/base.py.
* Выполните следующую команду для создания таблиц в базе данных:

```python3 db/base.py```

## Запуск приложения локально

*    Для запуска приложения, выполните следующую команду:

```uvicorn main:app``` 

После успешного запуска, API будет доступно по адресу (http://localhost:8000).

## Описание API

### Модели данных

1. Меню (Menu):
* id (uuid) - уникальный идентификатор меню.
* name (str) - название меню.
* description (str) - описание меню.

2. Подменю (SubMenu):
* id (uuid) - уникальный идентификатор подменю.
* name (str) - название подменю.
* description (str) - описание подменю.
* menu_id (uuid) - идентификатор меню, к которому привязано подменю.

3. Блюдо (Dish):
* id (uuid) - уникальный идентификатор блюда.
* name (str) - название блюда.
* description (str) - описание блюда.
* price (decimal) - цена блюда (с округлением до 2 знаков после запятой).
* submenu_id (uuid) - идентификатор подменю, к которому привязано блюдо.

## Операции API

API предоставляет следующие операции CRUD для каждой из сущностей (Меню, Подменю, Блюдо):

* `GET` __/api/v1/menus__: Получить список всех меню с количеством подменю и блюд в каждом меню.

*    `POST` __/api/v1/menus__: Создать новое меню.

*   `GET` __/api/v1/menus/{menu_id}__: Получить информацию о конкретном меню с количеством подменю и блюд в нем.

*   `PUT` __/api/v1/menus/{menu_id}__: Обновить информацию о меню.

*    `DELETE` __/api/v1/menus/{menu_id}__: Удалить меню и все привязанные к нему подменю и блюда.

*    `GET` __/api/v1/{menu_id}/submenus__: Получить список всех подменю определенного меню с количеством блюд в каждом подменю.

*   `POST` __/api/v1/{menu_id}/submenus__: Создать новое подменю.

*    `GET` __/api/v1/{menu_id}/submenus/{submenu_id}__: Получить информацию о конкретном подменю с количеством блюд в нем.

*    `PUT` __/api/v1/{menu_id}/submenus/{submenu_id}__: Обновить информацию о подменю.

*    `DELETE` __/api/v1/{menu_id}/submenus/{submenu_id}__: Удалить подменю и все привязанные к нему блюда.

*    `GET` __/api/v1/{menu_id}/submenus/{submenu_id}/dishes__: Получить список всех блюд.

*    `POST` __/api/v1/{menu_id}/submenus/{submenu_id}/dishes__: Создать новое блюдо для определенного подменю.

*    `GET` __/api/v1/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}__: Получить информацию о конкретном блюде.

*    `PUT` __/api/v1/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}__: Обновить информацию о блюде.

*    `DELETE` __/api/v1/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}__: Удалить блюдо.
