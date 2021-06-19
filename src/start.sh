#!/bin/sh
sleep 3

cd /code
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
