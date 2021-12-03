from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    task_title=models.CharField(max_length=200)
    task_description=models.TextField(max_length=2000,null=True)
    #task_img=models.ImageField(upload_to='task_images')
    time_stamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task_title

class Tasktables(models.Model):
    s_no=models.AutoField(primary_key=True)
    title=models.TextField(max_length=200)
    parent_id=models.IntegerField()
    def __str__(self):
        return self.title