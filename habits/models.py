from datetime import datetime
from email.policy import default

from django.db import models

# Create your models here.

class HabitUser(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='username')

class Habit(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    period = models.CharField(max_length=50)
    members = models.ManyToManyField(HabitUser, through='UserAndHabitMembership')

class UserAndHabitMembership(models.Model):
    user = models.ForeignKey(HabitUser, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.now)
    longest_steak = models.IntegerField(default=0)
    total_steak = models.IntegerField(default=0)
    current_steak = models.IntegerField(default=0)

class UserAndHabitMembershipLog(models.Model):
    submit_date = models.DateField()
    user_and_habit_membership = models.ForeignKey(UserAndHabitMembership, on_delete=models.CASCADE)
