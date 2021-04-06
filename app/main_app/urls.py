from django.urls import path, include
from .models import Admin_Coffee, User_Coffee, Favorites, Reviews
from . import views
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.home, name = 'home'),
    path('return' , views.home, name = 'return'),
    path('accounts/signup/', views.signup, name= 'signup'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/create/', views.coffee_create.as_view(), name = 'coffee_create'),
    path('api-auth/', include('rest_framework.urls')),
]
