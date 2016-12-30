#!/bin/sh

python manage.py collectstatic
git add -A
git commit
git push
eb deploy
