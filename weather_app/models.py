from django.db import models

# Create your models here.

class register(models.Model):
    name=models.CharField(max_length=20,)
    location=models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
    