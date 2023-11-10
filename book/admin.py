from django.contrib import admin
from .models import Room, Invitation, Notification, Land, House, LocalRoom

admin.site.register(Room)
admin.site.register(Invitation)
admin.site.register(Notification)
admin.site.register(Land)
admin.site.register(House)

class LocalRoomAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'state', 'town', 'address', 'phone_number',
    'is_available')

admin.site.register(LocalRoom)