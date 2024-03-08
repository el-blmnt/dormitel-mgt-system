from django.db import models

# Create your models here.

""" foreign key references (on_delete)
CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION. (2) """


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
    room_number = models.IntegerField(primary_key=True, unique=True, default="", null=False)
    room_description = models.TextField(default="", null=False)
    room_type = models.CharField(max_length = 20, default="")
    room_amount = models.FloatField(null=False)
    room_status = models.CharField(max_length=20, null=False)
    no_of_beds_available = models.IntegerField(null=False)
    room_image = models.CharField(max_length = 255, default = "")

class Bed(models.Model):
    bed_no = models.IntegerField()
    room_number = models.ForeignKey(Room, on_delete = models.CASCADE)
    bed_description = models.TextField()
    bed_amount = models.FloatField()
    bed_status = models.CharField(max_length = 20)

class Reservation(models.Model):
    reservation_code = models.CharField(max_length= 50, unique = True)
    reservation_date = models.DateField(auto_now_add = True) #date of reservation
    tentative_checkin = models.DateField() #tentative date when to occupy the reservation
    lodgerID = models.ForeignKey(Lodger, on_delete=models.CASCADE) #foreign key to Lodger

class Billing(models.Model):
    ORnumber = models.IntegerField(unique = True)
    lodgerID = models.ForeignKey(Lodger, on_delete=models.CASCADE) #foreign key to Lodger
    payment_date = models.DateField()
    payment_time = models.TimeField()
    particulars = models.CharField(max_length = 200)
    amount_due = models.FloatField()

class TransientCheckIn(models.Model):
    lodgerID = models.ForeignKey(Lodger, on_delete=models.CASCADE) # foreign key to Lodger
    checkinDate = models.DateField(auto_now_add = True)
    checkinTime = models.TimeField()