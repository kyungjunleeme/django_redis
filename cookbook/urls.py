from django.urls import path
# from django.urls import re_path

from . import views

urlpatterns = [
    # re_path(r'^$', views.recipes_view),
    path('', views.recipes_view),
]
