from django.urls import path
from . import views


urlpatterns = [
    path('our_rooms/', views.our_rooms, name='our_rooms'),
]