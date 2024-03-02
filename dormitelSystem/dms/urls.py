from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('sample/', views.sampleagain),
   path('rooms/', views.rooms)
]
