from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse_lazy
from book.models import Room, Invitation, Notification, LocalRoom, Land, House
from .models import OlaroomProfile, Olaroom, User, RealtorProfile
from .forms import InvitationForm, OlaroomSignUpForm, RealtorSignUpForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RoomForm, AddLandForm, AddHouseForm, AddLocalRoomForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class RealtorSignUpView(CreateView):
    model = Olaroom
    form_class = RealtorSignUpForm
    template_name = 'Login/create_user_for_realtor.html'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('Login')

def home(request):
    lands = Land.objects.filter(is_available=True)
    context = {'lands':lands}
    return render(request, 'home.html', context)

def local_rooms_views(request, slug):
    local_room = get_object_or_404(LocalRoom, slug=slug)
    context = {'local_room':local_room}
    return render(request, 'local_rooms_views.html', context)

def land(request):
    lands = Land.objects.filter(is_available=True)
    context = {'lands':lands}
    return render(request, 'land.htm', context)

def view_lands(request, slug):
    land = get_object_or_404(Land, slug=slug)
    land = {'land':land}
    return render(request, 'land_views.html', context)

def houses(request):
    houses = House.objects.filter(is_available=True)
    context = {'houses':houses}
    return render(request, 'house.html', context)

def view_houses(request, slug):
    house = get_object_or_404(House, slug=slug)
    context = {'house':house}
    return render(request, 'view_houses.html', context)

def hotel_rooms(request):
    rooms = Room.objects.filter(is_available=True)
    context = {'rooms':rooms}
    return render(request, 'hotel_room.html', context)

def view_hotel_room(reqauest, slug):
    room = get_object_or_404(Room, slug=slug)
    context = {'room':room}
    return render(request, 'view_hotel_room.html', context)

class CreateInvitationForRoom(CreateView):
    model = Invitation
    form_class = InvitationForm
    template_name = 'rooms_views.html'
    success_url = reverse_lazy('Success')

    def form_valid(self, form):
        return super(CreateInvitationForRoom, self).form_valid(form)











def rooms(request):
    rooms = Room.objects.filter(user=request.user)
    if request.user.is_authenticated and request.user.role == 'REALTOR':
        return redirect('Realtor_Dashboard')
        

    object_list = 5
    p = Paginator(rooms, object_list)
    page_number = request.GET.get('page')    

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    context = {'rooms':rooms, 'page_obj':page_obj}
    return render(request, 'Hotel/room_content.html', context)

def my_invitations(request, slug):
    if request.user.is_authenticated and request.user.role == 'REALTOR':
        return redirect('Realtor_Dashboard') 
    room = Room.objects.get(slug=slug)
    invitations = Invitation.objects.filter(room_type_id=room)

    object_list = 5
    p = Paginator(invitations, object_list)
    page_number = request.GET.get('page')    

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    context = {'invitations':invitations, 'page_obj':page_obj}
    return render(request, 'my_invitations.html', context)

def invitation_information(request, slug):
    if request.user.is_authenticated and user.role == 'REALTOR':
        return redirect('Realtor_Dashboard') 
    invitation = Invitation.objects.get(slug=slug)
    profiles = Profile.objects.filter(user=invitation.room_type.user)
    return render(request, 'invitations.html', {'invitation':invitation, 'profiles':profiles})

class CreateRoom(LoginRequiredMixin, CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'Hotel/create_room.html'
    success_url = reverse_lazy('Success')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'REALTOR':
            return redirect('Realtor_Dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateRoom, self).form_valid(form)

class Update_Room(LoginRequiredMixin, UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'Hotel/update_room.html'
    success_url = reverse_lazy('Success')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'REALTOR':
            return redirect('Realtor_Dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super(Update_Room, self).form_valid(form)

def notification(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    context = {'notifications':notifications}
    return render(request, 'notification.html', context)

class OlaroomSignUpView(CreateView):
    model = Olaroom
    form_class = OlaroomSignUpForm
    template_name = 'Login/create_user_for_olarooms.html'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('Login')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.role == User.Role.REALTOR:
                    auth_login(request, user)
                    return redirect('Realtor_Dashboard')
                elif user.role == User.Role.OLAROOM:
                    auth_login(request, user)
                    return redirect('Rooms')
                else:
                    messages.error(request, 'Invalid Creadentials')
    else:
        form = AuthenticationForm()        
    return render(request, 'Login/login.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect('/')





def realtor_dashboard(request):
    return render(request, 'Realtor/realtor_dashboard.html')

def realtor_profile(request):
    profiles = RealtorProfile.objects.filter(user=request.user)
    context = {'profiles':profiles}
    return render(request, 'Realtor/realtor_profile.html', context)

def land_user(request):
    lands = Land.objects.filter(user=request.user)
    context = {'lands':lands}
    return render(request, 'Realtor/land.html', context)

def Add_Land(request):
    if request.method == 'POST':
        form = AddLandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Land_Dashboard')
    else:
        form = AddLandForm()
    return render(request, 'Realtor/add_Land.html', {'form':form})

def house_user(request):
    houses = House.objects.filter(user=request.user)
    context = {'houses':houses}
    return render(request, 'Realtor/house.html', context)

def Add_House(request):
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('House_Dashboard')
    else:
        form = AddHouseForm()
    return render(request, 'Realtor/add_house.html', {'form':form})

def local_room_user(request):
    local_rooms = LocalRoom.objects.filter(user=request.user)
    context = {'local_rooms':local_rooms}
    return render(request, 'Realtor/local_room.html')

def Add_Local_Room(request):
    if request.method == 'POST':
        form = AddLocalRoomForm(request.POST)
        if form.is_valid:
            form.user = request.user
            form.save()
            return redirect('Local_Room')
    else:
        form = AddLocalRoomForm()
    return render(request, 'Realtor/add_local_room.html', {'form':form})
