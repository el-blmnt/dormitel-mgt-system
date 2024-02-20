from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .serializers import RoomSerializer
from .models import Rooms

from dms.forms import manageRooms

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer



def index(request, *arg, **kwargs):
    return render(request, 'frontend/index.html')

def sampleagain(request):
    return HttpResponse('Another text.')

def manageroomsform(request):
    form = manageRooms()
    context = {"form": form}
    return render(request, "rooms.html", context)