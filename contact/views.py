from django.shortcuts import render
from django.views.generic import CreateView
from contact.models import Contact
from django.urls import reverse_lazy


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'phone', 'message')
    success_url = reverse_lazy('catalog:category')
    