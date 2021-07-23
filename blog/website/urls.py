from django.urls import path, include
from .views import hello_blog, post_detail

urlpatterns = [
    path('', hello_blog, name='blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
]
