from datetime import datetime

from django.http import JsonResponse

from habits.models import HabitUser, Habit, UserAndHabitMembership, UserAndHabitMembershipLog


def serialize_membership(membership):
    return {'habit_name': membership.habit.title, 'total_steak': membership.total_steak,
            'longest_steak': membership.longest_steak, 'current_steak': membership.current_steak}


def serialize_user_for_rating(membership):
    return {'user_id': membership.user.id, 'username': membership.user.username, 'total_steak': membership.total_steak}


def dates_in_period(d_new, d_old, period):
    """ check if dates goes sequentially """
    if period == 'DAY':
        return (d_new - d_old).days < 2
    elif period == 'WEEK':
        return (d_new - d_old).days < 8


def create_user(request):
    request_data = request.POST
    user = HabitUser(email=request_data['email'], username=request_data['username'])
    user.save()
    return JsonResponse({'user_id': user.id})


def create_habit(request):
    request_data = request.POST
    habit = Habit(title=request_data['title'], description=request_data['description'], period=request_data['period'])
    habit.save()
    return JsonResponse({'habit_id': habit.id})


def register_user_for_habit(request):
    request_data = request.POST
    user = HabitUser.objects.get(id=request_data['user_id'])
    habit = Habit.objects.get(id=request_data['habit_id'])
    user_and_habit_membership = UserAndHabitMembership(user=user, habit=habit)
    user_and_habit_membership.save()
    return JsonResponse({'registred_habit_id': user_and_habit_membership.id})


def new_habit_action(request):
    request_data = request.POST
    user = HabitUser.objects.get(id=request_data['user_id'])
    habit = Habit.objects.get(id=request_data['habit_id'])
    submit_date = datetime.strptime(request_data['submit_date'], '%Y-%m-%d').date()
    # checked off logic
    user_and_habit_membership = UserAndHabitMembership.objects.get(user=user, habit=habit)
    user_and_habit_membership_log_last = UserAndHabitMembershipLog.objects.filter(user_and_habit_membership=user_and_habit_membership).last()
    user_and_habit_membership.total_steak += 1
    if not user_and_habit_membership_log_last:
        user_and_habit_membership.current_steak += 1
        user_and_habit_membership.longest_steak += 1
    elif dates_in_period(submit_date, user_and_habit_membership_log_last.submit_date, habit.period):
        user_and_habit_membership.current_steak += 1
        if user_and_habit_membership.current_steak > user_and_habit_membership.longest_steak:
            user_and_habit_membership.longest_steak = user_and_habit_membership.current_steak
    else:
        user_and_habit_membership.current_steak = 1
    user_and_habit_membership_log = UserAndHabitMembershipLog(submit_date=submit_date,
                                                              user_and_habit_membership=user_and_habit_membership)
    user_and_habit_membership_log.save()
    user_and_habit_membership.save()
    return JsonResponse(serialize_membership(user_and_habit_membership))
    

def get_user_info(request):
    request_data = request.POST
    user = HabitUser.objects.get(id=request_data['user_id'])
    habits = list(UserAndHabitMembership.objects.filter(user=user))
    habits = [serialize_membership(habit) for habit in habits]
    return JsonResponse(habits, safe=False)


def get_habit_rating(request):
    request_data = request.POST
    habit = Habit.objects.get(id=request_data['habit_id'])
    user_and_habit_memberships = UserAndHabitMembership.objects.filter(habit=habit).order_by('-total_steak')
    user_and_habit_memberships = [serialize_user_for_rating(membership) for membership in user_and_habit_memberships]
    return JsonResponse({'habit_name': habit.title, 'rating': user_and_habit_memberships})

    