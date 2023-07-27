from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES=[['Male','Male'],['Female','Female'],['Others','Others']]
class RegisterModel(User):
    
    contact=models.PositiveIntegerField()
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default=None)
    
   