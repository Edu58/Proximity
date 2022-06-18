from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class Neighbourhood(models.Model):
    name = models.CharField(blank=False, null=False, max_length=120)
    location = models.CharField(blank=False, null=False, max_length=60)
    number_of_occupants = models.IntegerField(blank=False, null=False)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

    def create_neighbourhood(self):
        self.save()

    def update_neighbourhood(self):
        self.save()

    def update_occupants(self, new_occupants):
        self.number_of_occupants = new_occupants
        self.save()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        try:
            neighbourhood = get_object_or_404(cls, pk=neigborhood_id)
        except:
            return None
        return neighbourhood

    def delete_neighbourhood(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='profile/')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=120)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(blank=False, null=False, max_length=60)
    time = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def save_announcement(self):
        self.save()

    def delete_announcement(self):
        self.delete()


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def save_alert(self):
        self.save()

    def delete_alert(self):
        self.delete()