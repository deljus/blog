## Simple django blog
Blog made using the django framework


#### Start the project in dev mode

1 Create a .env file in the root directory of the following content

```
SECRET_KEY=YOUR_RANDOM_KEY
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your_account@gmail.com
EMAIL_HOST_PASSWORD=your account’s password
EMAIL_PORT=587
MODE=development
```

2 Create virtual environment for python 3 in root directory

```
python3 -m venv venv
source venv/bin/activate
```

3 Install requirements

```
pip install -r requirements.txt
```

4 Make a database migration migration

```
pythom manage.py migrate
```

5 Start project

```
python manage.py runserver
```
