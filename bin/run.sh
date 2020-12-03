cd $(git rev-parse --show-toplevel)/boardsteam
python manage.py makemigrations
python manage.py migrate
python manage.py flush --noinput
python manage.py shell < add_content.py
python manage.py runserver
