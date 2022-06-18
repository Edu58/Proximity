from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


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
            'name',
            'description', 
        )