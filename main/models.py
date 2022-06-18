from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='profile/')
    city = models.CharField(blank=True, null=True, max_length=60)
    street = models.CharField(blank=True, null=True, max_length=60)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
