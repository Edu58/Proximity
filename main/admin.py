from django.contrib import admin
from .models import Profile, Category, Neighbourhood, Post


admin.site.register([
    Profile,
    Category, 
    Neighbourhood, 
    Post
])
