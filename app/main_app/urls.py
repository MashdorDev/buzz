from django.urls import path
from .models import Admin_Coffee, User_Coffee, Favorites, Reviews
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('return' , views.home, name = 'return'),
    path('accounts/signup/', views.signup, name= 'signup'),
    path('coffee/'), views.coffeeIndex, name= 'coffeeIndex'),
]
