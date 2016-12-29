#!/bin/sh

git add -A
git commit
git push
python manage.py collectstatic
eb deploy
