from django.db import models
import datetime

# Create your models here.
class user(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    email=models.EmailField(primary_key=True)
    
    def __str__(self):
        return self.email
    
class task(models.Model):
    taskId=models.AutoField(primary_key=True)
    taskname=models.CharField(max_length=50)
    taskdesc=models.CharField(max_length=300)
    email=models.EmailField()
    dateadded=models.DateTimeField()
    done=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.email+' '+str(self.taskId)
    