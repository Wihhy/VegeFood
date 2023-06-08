from django.urls import path
from .views import IndexView, ShopView, about, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop', ShopView.as_view(), name='shop'),
    path('about', about, name='about'),
    path('shop/<slug:slug>', ShopView.as_view(), name='category'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product-detail')
]
