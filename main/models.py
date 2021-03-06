from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.validators import MaxValueValidator


class Neighbourhood(models.Model):
    name = models.CharField(null=False, blank=False, max_length=120)
    location = models.CharField(blank=False, null=False, max_length=60)
    number_of_occupants = models.PositiveIntegerField(blank=False, null=False)
    health_dept_contact = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999999999999)]
    )
    police_dept_contact = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999999999999)]
    )
    fire_dept_contact = models.PositiveBigIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999999999999)]
    )
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

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
    def find_neigborhood(cls, name):
        try:
            neighbourhood = cls.objects.filter(name__icontains=name)
        except:
            return None

        return neighbourhood

    def delete_neighbourhood(self):
        self.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, blank=True, null=True
    )
    profile_pic = models.ImageField(blank=True, null=True, upload_to="profiles/")
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(blank=False, null=False, max_length=60)
    created_at = created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    neighbourhood = models.ForeignKey(
        Neighbourhood, related_name="hood_posts", on_delete=models.CASCADE
    )
    title = models.CharField(blank=False, null=False, max_length=120)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=120)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    business_contact = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999999999999)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name

    def create_business(self):
        self.save()

    def update_business(self):
        self.save()

    @classmethod
    def find_business(cls, business_name):
        try:
            business = cls.objects.filter(name__icontains=business_name)
        except:
            return None
        return business

    def delete_business(self):
        self.delete()
