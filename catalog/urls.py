from django.urls import path

from catalog.apps import MainConfig
from catalog.views import home, contacts

app_name = MainConfig.name

urlpatterns = [
    path("", home),
    path("contacts/", contacts)
]
