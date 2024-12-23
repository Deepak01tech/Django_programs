from django.db import models

# Create your models here.

class UserData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=75,unique=True)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)

    class Meta:
        db_table = "user_data"

    def __str__(self):
        return f'{self.name}'


