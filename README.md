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

# Examples of requsts to service (how to interact with system)

You can create and run them in postman

CREATE USER

```js
'url': '/habits/create_user',
'request_data': {'email': 'test1@test.com', 'username': 'test1'},
'response_data': {'user_id': 2}
```

CREATE HABIT

```js
'url': '/habits/create_habit',
'request_data': {'title': 'make push-ups', 'description': 'Make push-ups', 'period': 'DAY'},
'response_data': {'habit_id': 1}
```

REGISTER USER FOR HABIT

```js
'url': '/habits/register_user_for_habit',
'request_data': {'user_id': 2, 'habit_id': 1},
'response_data': {'registred_habit_id': 2}
```

USER SUBMIT FOR HABIT 

```js
'url': '/habits/new_habit_action',
'request_data': {'user_id': 1, 'habit_id': 1, 'submit_date': '2022-10-20'},
'response_data': {'habit_name': 'make push-ups', 'total_steak': 1, 'longest_steak': 1, 'current_steak': 1}
```

GET INFO ABOUT USER (RETURN INFO ABOUT USER HABITS)

```js
'url': '/habits/get_user_info',
'request_data': {'user_id': 1},
'response_data': [{'habit_name': 'make push-ups', 'total_steak': 2, 'longest_steak': 2, 'current_steak': 2}]
```


