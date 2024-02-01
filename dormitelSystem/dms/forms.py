from django import forms

ROOMTYPE = (
    ("1", "Ordinary"),
    ("2", "Airconditioned")
)

ROOMSTATUS = (
    ("1", "Vacant"),
    ("2", "Occupied"),
    ("3", "Under Renovation")
)

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class manageRooms(forms.Form):
    room_number = forms.IntegerField()
    room_description = forms.TextInput()
    room_type = forms.ChoiceField(choices= ROOMTYPE)
    room_amount = forms.FloatField()
    room_status = forms.ChoiceField(choices= ROOMSTATUS)
    no_of_beds_available = forms.IntegerField()