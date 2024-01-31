from django.db import models

# Create your models here.
class Lodger(models.Model):
    lodgerID = models.CharField(max_length = 50 unique = True)
    last_name = models.CharField(max_length = 100)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

