from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserLogoutView

app_name = 'auth'

urlpatterns = [
    path('registration', UserRegistrationView.as_view(), name='registration'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('profile/<pk>', UserProfileView.as_view(), name='profile')
]
