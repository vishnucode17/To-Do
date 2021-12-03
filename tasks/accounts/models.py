from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
# Create your models here.
# 1. User
# - uid (Primary key, auto increment)
# - username (unique => should start with a/A and end with 1/0)
# - join_date (datetime)
# - password (use sha 256 hash)
def username_validation(user_name):
    if user_name.startswith('a') or user_name.startswith('A'):
        if user_name.endswith('0') or user_name.endswith('1'):
            return True
class User(AbstractBaseUser):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,unique=True,validators=[username_validation])
    join_date=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=256)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    def __str__(self):
        return self.username
    