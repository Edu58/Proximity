from django.contrib import admin
from .models import Profile, Event, Announcement, Alert, Category


admin.site.register([
    Profile,
    Category,
    Event,
    Announcement,
    Alert
])
