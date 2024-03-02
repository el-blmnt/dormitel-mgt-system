from django.contrib import admin
from .models import Rooms

# Register your models here.

class RoomAdmin(admin.ModelAdmin): #to format the admin side dtb in tabular format
    list_display = ('room_number', 'room_description', 'room_type','room_amount', 'room_status', 'no_of_beds_available')

admin.site.register(Rooms, RoomAdmin)


