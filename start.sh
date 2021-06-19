#!/bin/sh
cd /code

# example create app : python manage.py startapp payments
# python manage.py inspectdb > payments/new_models_legacy.py
# python manage.py makemigrations payments
# python manage.py migrate payments
python manage.py runserver 0.0.0.0:8003
