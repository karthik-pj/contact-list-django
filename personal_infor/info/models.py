from django.db import models

# Create your models here.

class Info(models.Model):
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=50)
    relationship=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name