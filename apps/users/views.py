from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
User = get_user_model()


class UserRegistrationView(CreateView):
    template_name = 'auth/registration.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Sign-Up'
        return context


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = UserLoginForm
    next_page = reverse_lazy('shop:shop')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Login'
        return context


class UserLogoutView(LogoutView):
    template_name = 'auth/login.html'
    next_page = reverse_lazy('shop:index')


class UserProfileView(UpdateView):
    model = User
    template_name = 'auth/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        if referer:
            return referer
        else:
            return reverse('shop:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Profile'
        return context

