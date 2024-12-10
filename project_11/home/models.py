from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    father_name = models.CharField(max_length=100)

    class Meta:
        db_table = "student_table"