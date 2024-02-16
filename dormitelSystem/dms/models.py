from django.db import models

# Create your models here.
class Lodger(models.Model): 
    lodgerID = models.CharField(max_length = 50, unique = True, null=False)
    last_name = models.CharField(max_length = 100,null=False)
    first_name = models.CharField(max_length=50, null=False)
    contact_number = models.IntegerField()
    home_address = models.CharField(max_length = 100)
    email_address = models.EmailField(null=False)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    schedule_of_last_due = models.DateField() 
    schedule_of_next_payment = models.DateField() 

class Rooms(models.Model):
    room_number = models.IntegerField(unique=True, null=False)
    room_description = models.TextField(null=False)
    room_type = models.CharField(max_length = 20)
    room_amount = models.FloatField(null=False)
    room_status = models.CharField(max_length=20, null=False)
    no_of_beds_available = models.IntegerField(null=False)

class Beds(models.Model):
    bed_no = models.IntegerField()
    room_number = models.IntegerField() #Assign as foreign key to the room number in rooms class
    bed_description = models.TextField()
    bed_amount = models.FloatField()
    bed_status = models.CharField(max_length = 20)

class Reservation(models.Model):
    reservation_code = models.CharField(max_length= 50, unique = True)
    reservation_date = models.DateField() 
    reservation_time = models.TimeField()
    lodgerID = models.IntegerField() #declare as foreign key to Lodger

class Billing(models.Model):
    ORnumber = models.IntegerField()
    lodgerID = models.IntegerField() #declare as foreign key to Lodger
    payment_date = models.DateField()
    payment_time = models.TimeField()
    particulars = models.CharField(max_length = 100)
    amount_due = models.FloatField()

class TransientCheckIn(models.Model):
    lodgerID = models.IntegerField() #declare as foreign key to Lodger
    



