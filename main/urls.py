from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('post/<post_id>', views.post_detail, name='post_detail'),
    path('post/', views.post, name='post'),
    path('hoods/', views.hoods, name='hoods'),
    path('hood/<hood_id>', views.hood_detail, name='hood-detail'),
    path('add-hood/', views.add_hood, name='add-hood'),
    path('add-business/', views.add_business, name='add-business'),
    path('businesses/', views.businesses, name='businesses'),
    path('profile/<username>/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
