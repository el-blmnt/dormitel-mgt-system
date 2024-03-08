from django.contrib import admin
from .models import Room, Lodger, Bed, Reservation, Billing, TransientCheckIn

# Register your models here.

class RoomAdmin(admin.ModelAdmin): #to format the admin side dtb in tabular format
    list_display = ('room_number', 'room_description', 'room_type','room_amount', 'room_status', 'no_of_beds_available')

class LodgerAdmin(admin.ModelAdmin):
    list_display = ('lodgerID', 'last_name', 'first_name', 'contact_number', 'home_address', 'email_address', 'username', 'password', 'schedule_of_last_due', 'schedule_of_next_payment')


admin.site.register(Room, RoomAdmin)
admin.site.register(Lodger, LodgerAdmin)
admin.site.register(Bed)
admin.site.register(Reservation)
admin.site.register(Billing)
admin.site.register(TransientCheckIn)


