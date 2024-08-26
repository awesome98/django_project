# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post-list', views.PostList.as_view()),
    path('about-me', views.about_me)
]