from django.urls import path
from .views import AboutView, ContactsView

app_name = 'about'

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('contacts', ContactsView.as_view(), name='contacts')
]


