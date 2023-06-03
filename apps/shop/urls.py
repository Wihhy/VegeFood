from django.urls import path
from .views import IndexView, shop, about

app_name = 'shop'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop', shop, name='shop'),
    path('about', about, name='about')
]
