from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=30,blank=False)
    dob = models.DateField(blank=False)
    address = models.TextField(max_length=150, blank=False)

    def __str__(self):
        return self.username
