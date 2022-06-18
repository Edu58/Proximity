from django.db import models
from django.contrib.auth.models import User

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


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Event(models.Model):
    name = models.CharField(blank=True, null=True, max_length=120)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(blank=False, null=False, max_length=60)
    time = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()


class Announcement(models.Model):
    name = models.CharField(blank=True, null=True, max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save_announcement(self):
        self.save()

    def delete_announcement(self):
        self.delete()