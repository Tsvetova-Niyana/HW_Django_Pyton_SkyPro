from django.urls import path

from blogs.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blogs.apps import BlogsConfig


app_name = BlogsConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name='list'),
    path("create", BlogCreateView.as_view(), name='create'),
    path("view/<int:pk>", BlogDetailView.as_view(), name='view'),
    path("update/<int:pk>", BlogUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name='delete'),
    # path("contacts/", ContactListView.as_view(), name='contacts'),
    # path("product/<int:pk>", ProductDetailView.as_view(), name='card')
]
