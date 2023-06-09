from pprint import pprint
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Product, Category
from django.http import Http404


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        categories = Category.objects.all()
        context['categories'] = {}
        for category in categories:
            context['categories'][f'{category.name.lower()}'] = {
                'name': category.name,
                'image_url': category.image.url,
                'slug': category.slug
            }
        context['title'] = 'VegeFoods'
        context['products'] = Product.objects.all()[:8]
        return context


class ShopView(ListView):
    template_name = 'shop/shop.html'
    queryset = Product.objects.all()
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'VegeFoods - Shop'
        context['categories'] = Category.objects.all()
        pprint(context)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        try:
            category = get_object_or_404(Category, slug=slug)
            category_id = category.id
        except Http404:
            return queryset
        return queryset.filter(category_id=category_id)


class ProductDetailView(DetailView):
    template_name = 'shop/product-single.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


