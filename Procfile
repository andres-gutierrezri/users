web: python manage.py collectstatic && python manage.py makemigrations && python manage.py migrate && gunicorn djangocrud.wsgi:application --workers 3 --log-file -