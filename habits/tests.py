from django.test import TestCase, Client

from habits.fixtures import fixtures

client = Client()


class HabitTests(TestCase):

    def test_all_logic(self):
        """Test all api logic"""

        # 1) create user
        response = self.client.post('/habits/create_user', {'email': 'test@test.com', 'username': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'user_id': 1})
        print('CREATE USER SUCCESSFULLY')

        # 2) create habit
        response = self.client.post('/habits/create_habit', {'title': 'make push-ups', 'description': 'Make push-ups', 'period': 'DAY'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'habit_id': 1})
        print('CREATE HABIT SUCCESSFULLY')

        # 3) register user for habit
        response = self.client.post('/habits/register_user_for_habit', {'user_id': 1, 'habit_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'registred_habit_id': 1})
        print('REGISTER USER FOR HABIT SUCCESSFULLY')

        # 4) checked off by user 1
        response = self.client.post('/habits/new_habit_action', {'user_id': 1, 'habit_id': 1, 'submit_date': '2022-10-20'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'habit_name': 'make push-ups', 'total_steak': 1, 'longest_steak': 1, 'current_steak': 1})
        print('CHECKED OFF BY USER SUCCESSFULLY 1')

        # 5) checked off by user 2
        response = self.client.post('/habits/new_habit_action', {'user_id': 1, 'habit_id': 1, 'submit_date': '2022-10-21'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'habit_name': 'make push-ups', 'total_steak': 2, 'longest_steak': 2, 'current_steak': 2})
        print('CHECKED OFF BY USER SUCCESSFULLY 2')

        # 5) get user info
        response = self.client.post('/habits/get_user_info', {'user_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'habit_name': 'make push-ups', 'total_steak': 2, 'longest_steak': 2, 'current_steak': 2}])
        print('GET USER SUCCESSFULLY')

        # 6) get user rating for habit
        response = self.client.post('/habits/get_habit_rating', {'habit_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'habit_name': 'make push-ups', 'rating': [{'user_id': 1, 'username': 'test', 'total_steak': 2}]})
        print('GET USER RATING SUCCESSFULLY')

        for fixture in fixtures:
            print(fixture)
            response = self.client.post(fixture['url'], fixture['request_data'])
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), fixture['response_data'])


        