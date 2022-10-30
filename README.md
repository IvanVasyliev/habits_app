# habits_app

if you want to install app run following commands:

1. create virtual env (optional)
```console
python3 -m venv env
source env/bin/activate
```

2. install dependencies, run database migrations and start server

```console
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

3. if you want to test app you can run

```console
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

4. for testing you can run this command 

```console
python manage.py test
```

You can find test data in `./habits/fixtures.py`

5. Examples of requsts to service (how to interact with system)

You can create and run them in postman

CREATE USER

```js
'url': '/habits/create_user',
'request_data': {'email': 'test1@test.com', 'username': 'test1'},
'response_data': {'user_id': 2}
```
