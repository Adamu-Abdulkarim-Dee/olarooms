from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('room_view/<slug:slug>/', views.local_rooms_views, name='Local_Room_Views'),

    path('realtor_dashboard/', views.realtor_dashboard, name='Realtor_Dashboard'),
    path('realtor_profile/', views.realtor_profile, name='Realtor_Profile'),

    path('land_list/', views.land_user, name='Land_Dashboard'),
    path('add_land/', views.Add_Land, name='Add_Land'),

    path('house_list/', views.house_user, name='House_Dashboard'),
    path('add_house/', views.Add_House, name='Add_House'),

    path('local_room_list/', views.local_room_user, name='Local_Room_Dashbaord'),
    path('add/', views.Add_Local_Room, name='Add_Local_Room'),

    path('login/', views.login, name='Login'),
    path('RealtorSignUpView/', views.RealtorSignUpView.as_view(), name='RealtorSignUpView'),

    path('rooms/', views.rooms, name='Rooms'),
    path('create-room/', views.CreateRoom.as_view(), name='Create_Room'),
    path('Update_Room/<slug:slug>/', views.Update_Room.as_view(), name='Update_Room'),
    path('invitation/<slug:slug>/', views.my_invitations, name='Invitation'),
    path('invitation_information/<slug:slug>/', views.invitation_information, name='invitation_information'),
    path('notification/', views.notification, name='Notifications'),
    path('OlaroomSignUpView/', views.OlaroomSignUpView.as_view(), name='OlaroomSignUpView'),
]