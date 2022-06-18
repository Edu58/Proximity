from django.contrib import admin
from .models import Profile, Event, Announcement, Alert


admin.site.register([
    Profile,
    Event,
    Announcement,
    Alert
])
