from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address= models.CharField(max_length=255)
    phone= models.IntegerField()

class Meta:
    db_table = 'users'

def __str__(self):
    return self.name


