#web: gunicorn rev_eng.wsgi
web: python manage.py collectstatic; gunicorn rev_eng2.wsgi --workers=4 --bind=0.0.0.0:$PORT 
