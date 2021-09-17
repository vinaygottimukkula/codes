
from django.db import models
from django.db.models.aggregates import Min
# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    roolnumber=models.IntegerField()
    dateofbirth=models.IntegerField()


    def __str__(self):                                                 # There is double underscore both sides
        return self.firstname