from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('return' , views.home, name = 'return'),
    path('accounts/signup/', views.signup, name= 'signup'),
]
