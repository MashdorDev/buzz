from django.urls import path
from .models import Admin_Coffee, User_Coffee, Reviews
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('return' , views.home, name = 'return'),
    path('accounts/signup/', views.signup, name= 'signup'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/create/', views.coffee_create.as_view(), name = 'coffee_create')
]
