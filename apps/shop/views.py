from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Product


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context = {
            'title': 'VegeFoods',
            'products': Product.objects.all()[:8]
        }
        return context


class ShopView(ListView):
    template_name = 'shop/shop.html'
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'VegeFoods - Shop'

def shop(request):
    context = {
        'title': 'VegeFoods - Shop'
    }
    return render(request, 'shop/shop.html', context=context)


def about(request):
    context = {
        'title': 'VegeFoods - About'
    }
    return render(request, 'Vegefoods/about.html', context=context)
