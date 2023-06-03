from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'VegeFoods'
        return context



# def index(request):
#     context = {
#         'title': 'VegeFoods'
#     }
#     return render(request, 'shop/index.html', context=context)


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
