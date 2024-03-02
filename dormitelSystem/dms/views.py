from django.shortcuts import render
from django.http import HttpResponse
from .models import Rooms

from dms.forms import manageRooms

# Create your views here.
def index(request):
    return render(request, "index.html")

def sampleagain(request):
    return HttpResponse('Another text.')

""" def manageroomsform(request):
    form = manageRooms()
    context = {"form": form}
    return render(request, "rooms.html", context) """

def rooms(request):
    rooms = Rooms.objects.all() #to retrive all data in dtb
    return render(request, "rooms.html", {'rooms': rooms}) # arg2: name of the template, arg3: data to be passed to arg2