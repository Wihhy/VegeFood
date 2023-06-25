from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'Введіть e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'Введіть пароль'}))

    # class Meta:
    #     model = User
    #     fields = ['email', 'password']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'Степан'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'Бандера'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'stepan@bandera.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'Введіть пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-left px-3', 'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    country = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    postcode = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-left px-3'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'country',
                  'city', 'phone_number', 'postcode', 'street_address')


