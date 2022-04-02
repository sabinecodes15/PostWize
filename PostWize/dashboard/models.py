import imp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User, UserManager

#user = UserManager.create_user(username, email, password)

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.first_name()

class Job(models.Model):
    job_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name()