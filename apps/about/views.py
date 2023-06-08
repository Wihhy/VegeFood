from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'VegeFoods - About'


class ContactsView(TemplateView):
    template_name = 'about/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'VegeFoods - Contacts'
