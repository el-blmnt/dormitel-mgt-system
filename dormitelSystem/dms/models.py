from django.db import models

# Create your models here.
class Lodger(models.Model): 
    lodgerID = models.CharField(max_length = 50, default="", unique = True, null=False)
    last_name = models.CharField(max_length = 100, default="", null=False)
    first_name = models.CharField(max_length=50, default="", null=False)
    contact_number = models.IntegerField()
    home_address = models.CharField(max_length = 100, default="")
    email_address = models.EmailField(default="", null=False)
    username = models.CharField(max_length = 50, default="")
    password = models.CharField(max_length = 50, default="")
    schedule_of_last_due = models.DateField() 
    schedule_of_next_payment = models.DateField() 

class Room(models.Model):
    room_number = models.IntegerField(unique=True, default="", null=False)
    room_description = models.TextField(default="", null=False)
    room_type = models.CharField(max_length = 20, default="")
    room_amount = models.FloatField(null=False)
    room_status = models.CharField(max_length=20, null=False)
    no_of_beds_available = models.IntegerField(null=False)

class Bed(models.Model):
    bed_no = models.IntegerField()
    room_number = models.IntegerField() #Assign as foreign key to the room number in rooms class
    bed_description = models.TextField()
    bed_amount = models.FloatField()
    bed_status = models.CharField(max_length = 20)

class Reservation(models.Model):
    reservation_code = models.CharField(max_length= 50, unique = True)
    reservation_date = models.DateField(auto_now_add = True) #date of reservation
    tentative_checkin = models.DateField() #tentative date when to occupy the reservation
    lodgerID = models.IntegerField() #declare as foreign key to Lodger

class Billing(models.Model):
    ORnumber = models.IntegerField(unique = True)
    lodgerID = models.IntegerField() #declare as foreign key to Lodger
    payment_date = models.DateField()
    payment_time = models.TimeField()
    particulars = models.CharField(max_length = 200)
    amount_due = models.FloatField()

class TransientCheckIn(models.Model):
    lodgerID = models.IntegerField() #declare as foreign key to Lodger
    checkinDate = models.DateField(auto_now_add = True)
    checkinTime = models.TimeField()

class room_gallery(models.Model):
    room_number= models.IntegerField() #assign foreign key for rooms
    room_image = models.ImageField()




