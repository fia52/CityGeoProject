# CityGeoProject
HTTP API, с помощью которого можно:

- Добавлять/удалять в хранилище информацию о городах
- Запрашивать информацию о городах из хранилища
- По заданным широте и долготе точки выдавать 2 ближайших к ней города из присутствующих в хранилище

## Технологии
- Django
- Django REST Framework
- PostgreSQL
- PostGIS

## Использование
Заполнить файл с перемнными огружения ".env";

Установить расширение PostGIS для своей PostgreSQL базы данных
```sh
$ sudo apt-get install postgis
$ sudo -i -u ИМЯ_ПОЛЬЗОВАТЕЛЯ_СУБД
$ psql -d ИМЯ_БАЗЫ_ДАННЫХ
$ #CREATE EXTENSION postgis;
```
Установите необходимые зависимости
```sh
$ pip install -r requirements.txt
```
Запустите сервер
```sh
$ python3 manage.py runserver
```
