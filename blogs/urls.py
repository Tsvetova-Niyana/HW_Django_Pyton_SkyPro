from django.urls import path

from blogs.views import BlogListView, BlogDetailView
from blogs.apps import BlogsConfig


app_name = BlogsConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name='list'),
    path("view/<int:pk>", BlogDetailView.as_view(), name='view'),
    # path("contacts/", ContactListView.as_view(), name='contacts'),
    # path("product/<int:pk>", ProductDetailView.as_view(), name='card')
]
