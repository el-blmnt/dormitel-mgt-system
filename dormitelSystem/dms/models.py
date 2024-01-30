from django.db import models

# Create your models here.
class Accounts(models.Model):
    accountID = models.IntegerField()
    fullname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

