#!/bin/sh

python manage.py collectstatic
eb deploy
