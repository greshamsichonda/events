from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#funs table
class Funs(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    residence=models.CharField(max_length=120)
    def __str__(self):
        return self.first_name 
    
#venue table
class Venues(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    phone=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
#events table    
class Events(models.Model):
    name=models.CharField(max_length=120)
    event_date=models.DateTimeField()
    #venue=models.CharField(max_length=120)
    venue=models.ForeignKey(Venues, blank=True, null=True, on_delete=models.CASCADE)
    description=models.TextField(max_length=120)
    manager=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    funs=models.ManyToManyField(Funs, blank=True)   
    def __str__(self):
        return self.name
    
