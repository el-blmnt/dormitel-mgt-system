from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

from dms.forms import manageRooms

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signUp.html")

def sampleagain(request):
    return HttpResponse('Another text.')

def manageRoom(request):
    form = manageRooms()
    context = {"form": form}
    return render(request, "manageroom.html", context)

def rooms(request):
    rooms = Room.objects.all() #to retrive all data in dtb
   # rooms = Room.objects.get(id=pk) #to retrive specific data
    return render(request, "rooms.html", {'room': rooms}) # arg2: name of the template, arg3: data to be passed to arg2

