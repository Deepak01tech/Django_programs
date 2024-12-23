from django.db import models

# Create your models here.


class employee(models.Model):
    name=models.CharField()
    email=models.EmailField()
    address=models.CharField()
    eid=models.CharField(max_length=10)
    phone=models.CharField()
    
    class Meta:
        db_table='employee'
    def __str__(self):
        return f'{self.eid}-{self.name}'