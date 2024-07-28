from django.db import models

# Create your models here.
class studentDB(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    age=models.IntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=10)
