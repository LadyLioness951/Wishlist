from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_index, name='wishlist_index'),
]