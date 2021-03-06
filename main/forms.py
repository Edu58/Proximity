from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Neighbourhood, Business


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("user", )
        fields = (
            'category',
            'neighbourhood',
            'title',
            'description',
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["neighbourhood","profile_pic", "bio",]


class AddNeighbourhood(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = '__all__'


class AddBusiness(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Business
        fields = ['name', 'neighbourhood', 'email','business_contact']