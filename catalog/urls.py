from django.urls import path

from catalog.apps import MainConfig
from catalog.views import ProductListView, ContactListView, ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='home'),
    path("contacts/", ContactListView.as_view(), name='contacts'),
    path("product/<int:pk>", ProductDetailView.as_view(), name='card')
]
