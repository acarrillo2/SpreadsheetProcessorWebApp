# Developer Notes: SpreasheetProcessorWebApp

To set up django and a virtual environment follow these instructions:
https://code.visualstudio.com/docs/python/tutorial-django

If you already have a virtual environment run:
```
source env/bin/activate
```

To set up database and apply change from code run:
```
python src/manage.py migrate
```

To run the dev server run:
```
python src/manage.py runserver
```

To create a new secret key:
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```