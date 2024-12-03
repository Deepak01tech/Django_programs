from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'students_table'

