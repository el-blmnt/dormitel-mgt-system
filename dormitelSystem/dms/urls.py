from django.urls import path
from . import views
from .views import RoomView

urlpatterns = [
   path('', views.index),
   path('sample/', views.sampleagain),
   #path('manage-rooms/', views.manageroomsform)
   path('manage-rooms/', RoomView.as_view()),
]
