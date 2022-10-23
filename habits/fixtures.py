fixtures = [
    {
        'url': '/habits/create_user',
        'request_data': {'email': 'test1@test.com', 'username': 'test1'},
        'response_data': {'user_id': 2}
    },
    {
        'url': '/habits/register_user_for_habit',
        'request_data': {'user_id': 2, 'habit_id': 1},
        'response_data': {'registred_habit_id': 2}
    },
    {
        'url': '/habits/new_habit_action',
        'request_data': {'user_id': 2, 'habit_id': 1, 'submit_date': '2022-10-10'},
        'response_data': {'habit_name': 'make push-ups', 'total_steak': 1, 'longest_steak': 1, 'current_steak': 1}
    },
    {
        'url': '/habits/new_habit_action',
        'request_data': {'user_id': 2, 'habit_id': 1, 'submit_date': '2022-10-11'},
        'response_data': {'habit_name': 'make push-ups', 'total_steak': 2, 'longest_steak': 2, 'current_steak': 2}
    },
    {
        'url': '/habits/new_habit_action',
        'request_data': {'user_id': 2, 'habit_id': 1, 'submit_date': '2022-10-12'},
        'response_data': {'habit_name': 'make push-ups', 'total_steak': 3, 'longest_steak': 3, 'current_steak': 3}
    },
    {
        'url': '/habits/new_habit_action',
        'request_data': {'user_id': 2, 'habit_id': 1, 'submit_date': '2022-10-15'},
        'response_data': {'habit_name': 'make push-ups', 'total_steak': 4, 'longest_steak': 3, 'current_steak': 1}
    },
    {
        'url': '/habits/get_habit_rating',
        'request_data': {'habit_id': 1},
        'response_data': {'habit_name': 'make push-ups', 
                          'rating': [{'user_id': 2, 'username': 'test1', 'total_steak': 4}, 
                                     {'user_id': 1, 'username': 'test', 'total_steak': 2}]}
    },
]
