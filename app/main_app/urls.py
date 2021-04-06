from django.urls import path, include
from .models import Admin_Coffee, User_Coffee, Reviews
from . import views
from rest_framework import routers, serializers, viewsets



urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/signup/', views.signup, name= 'signup'),
    path('coffee/', views.coffee_index, name='coffee_index'),
    path('store/', views.store_index, name='store_index'),
    path('coffee/create/', views.coffee_create.as_view(), name = 'coffee_create'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('profile/favorites', views.index_favorites, name='favorites'),
    path('topdrinks/', views.index_top_drinks, name='top_drinks'),
    path('topshops/', views.index_top_shops, name='top_shops'),
    path('type/cof', views.index_type_cof, name='type_cof'),
    path('type/ice', views.index_type_ice, name='type_ice'),
    path('type/esp', views.index_type_esp, name='type_esp'),
    path('type/cap', views.index_type_cap, name='type_cap'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/create/', views.coffee_create.as_view(), name = 'coffee_create'),
    path('api-auth/', include('rest_framework.urls')),
]
