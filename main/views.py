from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from .forms import SignUpForm, LoginUserForm, PostForm, UpdateProfileForm, UserUpdateForm, AddBusiness, AddNeighbourhood
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Business, Neighbourhood, Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')


def signup_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

        messages.warning(request, 'Please provide the required credentials!')
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')

        messages.warning(request, 'Invalid email or password!')
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def home(request):
    all_posts = Post.objects.all()

    [post for post in all_posts]

    context = {
        'posts': all_posts,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def post_detail(request, post_id):

    try:
        post = get_object_or_404(Post, pk=post_id)
    except Post.DoesNotExist:
        return None

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)


@login_required(login_url='login')
def post(request):
    form = PostForm()

    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            messages.success(request, 'Post uploaded successfully')
            return redirect('home')

        messages.warning(request, 'Please provide valid data')
        return render(request, 'post.html', {'form': form})

    context = {'form': form}

    return render(request, 'post.html', context)


@login_required(login_url='login')
def hoods(request):

    hoods = Neighbourhood.objects.all()

    if request.method == "POST":
        query = request.POST.get('hood-query')
        results = Neighbourhood.find_neigborhood(query)

        context = {
            'hoods': results,
        }

        return render(request, 'hoods.html', context)

    context = {'hoods': hoods}

    return render(request, 'hoods.html', context)


@login_required(login_url='login')
def hood_detail(request, hood_id):

    hood = get_object_or_404(Neighbourhood, pk=hood_id)

    context = {'hood': hood}

    return render(request, 'hood-detail.html', context)


@login_required(login_url='login')
def add_hood(request):
    form = AddNeighbourhood()

    if request.method == "POST":
        form = AddNeighbourhood(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Neighbourhood created successfully')
            return redirect('hoods')

    context = {'form': form}
    return render(request, 'add-hood.html', context)


@login_required(login_url='login')
def businesses(request):

    businesses = Business.objects.all()

    if request.method == "POST":
        query = request.POST.get('business-query')
        results = Business.find_business(query)

        context = {
            'businesses': results,
        }

        return render(request, 'businesses.html', context)


    context = {'businesses': businesses}

    return render(request, 'businesses.html', context)


@login_required(login_url='login')
def add_business(request):
    form = AddBusiness()

    if request.method == "POST":
        form = AddBusiness(request.POST)

        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.save()
            messages.success(request, 'Business created successfully')
            return redirect('businesses')

    context = {'form': form}
    return render(request, 'add-business.html', context)


@login_required(login_url='login')
def profile(request, username):
    user = get_object_or_404(User, username=username)

    can_update = False

    if request.user == user:
        can_update = True
    else:
        can_update = False

    context = {'user': user, 'can_update': can_update}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def update_profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('profile', args=[request.user]))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {'user_form': user_form, 'prof_form': profile_form}

    return render(request, 'update-profile.html', context)


@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')