from django.shortcuts import render
from django.http import HttpResponse

from dms.forms import manageRooms

# Create your views here.
def index(request):
    return render(request, "index.html")

def sampleagain(request):
    return HttpResponse('Another text.')

def manageroomsform(request):
    form = manageRooms()
    context = {"form": form}
    return render(request, "rooms.html", context)