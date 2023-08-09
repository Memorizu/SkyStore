from contact.views import ContactCreateView
from contact.apps import ContactConfig
from django.urls import path


app_name = ContactConfig.name


urlpatterns = [
    path('', ContactCreateView.as_view(), name='contacts')  
]