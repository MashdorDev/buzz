from django.urls import path, include
from .models import Admin_Coffee, User_Coffee, Reviews
from . import views



urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/signup/', views.signup, name= 'signup'),
    path('store/<str:store_id>/', views.store_details, name='store_details'),
    path('coffee/detail/<int:coff_id>/', views.coffee_detail, name='coffee_detail'),
    path('coffee/create/<str:store_id>/', views.coffee_create, name='coffee_create'),
    path('addreview/<int:coff_id>/', views.create_review, name='review_create'),
    path('search/', views.search, name='search'),
    path('searching/', views.searching, name='searching'),
    path('profile/favorites/', views.index_favorites, name='favorites'),
    path('topdrinks/', views.index_top_drinks, name='top_drinks'),
    path('topshops/', views.index_top_shops, name='top_shops'),
    path('type/cof', views.index_type_cof, name='type_cof'),
    path('type/ice', views.index_type_ice, name='type_ice'),
    path('type/esp', views.index_type_esp, name='type_esp'),
    path('type/cap', views.index_type_cap, name='type_cap'),
    path('profile/', views.profile, name='profile'),
    path('approval/admin', views.admin_approval, name='admin_approval'),
    path('approved/<int:cof_id>', views.approved, name='approved'),
    path('delete/admin/<int:cof_id>', views.delete_ad, name='delete_ad'),
    path('profile/avatar/', views.create_avatar, name='profile_avatar'),
]
