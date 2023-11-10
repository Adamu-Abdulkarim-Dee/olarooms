from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Olaroom, Realtor
from django import forms
from book.models import Room, Invitation, Land, House, LocalRoom

class OlaroomSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Olaroom
        fields = ['username', 'email', 'company_name', 'address', 'phone_number', 'country']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.role == User.Role.OLAROOM
            if commit:
                user.save()
            return user

class RealtorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Realtor
        fields = ['username', 'email', 'first_name', 'last_name', 'address', 'phone_number', 'country', 'state']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.role == User.Role.REALTOR
            if commit:
                user.save()
            return user

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['first_name', 'last_name', 'email', 'phone_number', ]

class RoomForm(forms.ModelForm):
    is_available = forms.TypedChoiceField(coerce=lambda x: x=='True',
    choices=((False, 'No'), (True, 'Yes')))
    class Meta:
        model = Room
        fields = ['room_name', 'price', 'currency', 'country', 'state',
        'address', 'description', 'image_1', 'image_2', 'image_3', 'image_4', 'town', 'is_available']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

class AddLandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['land_type', 'country', 'state', 'town', 'land_address', 'phone_number',
        'currency', 'price', 'image_1', 'image_2', 'image_3', 'image_4', 'description']

class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['house_type', 'country', 'state', 'town', 'house_address', 'phone_number', 
        'currency', 'price', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'description']

class AddLocalRoomForm(forms.ModelForm):
    class Meta:
        model = LocalRoom
        fields = ['country']
