from django.db import models
import os
from django.contrib.auth.models import User

def some_function(request):
    my_key = os.environ['SECRET_KEY']

TYPES = (
    ('C', 'Cafe Bought'),
    ('S', 'Store Bought Home Made')
)

CATEGORIES = (
    ('C', 'Cold Coffe'),
    ('D', 'Decaffeinated'),
    ('IC', 'Iced Coffe'),
    ('R', 'Regular Coffe'),
)

# User model many to one with favorites, reviews, admin coffe and user coffe
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')
    admincof = models.ForeignKey(Admin_Coffe, on_delete=models.CASCADE)
    usercof = models.ForeignKey(User_Coffe, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.user.username

# Tracking user favorites many to one for users and many to many for coffes
class Favorites(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    coffe = models.ManyToManyField(Admin_Coffe)
    
    def _str_(self):
        return "%S %S" % (self.profile.user.username, self.coffe.name)

# many to one for users and coffee
class Reviews(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review = models.CharField( max_length=1000)
    rating = models.IntegerField()
    coffe = models.ForeignKey(Admin_Coffe, on_delete=models.CASCADE)

    def _str_(self):
        return "%S %S" % (self.profile.user.username, self.coffe.name)

# many to one for users 
class Admin_Coffe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cof_type = models.CharField('type', max_length=1, choices=TYPES, default=MEALS[0][0])
    categories = models.CharField('categories', max_length=1, choices=CATEGORIES, default=MEALS[0][0])
    photo = models.ImageField(upload_to='coffe')
    rating = models.IntegerField()
    Favorites = models.IntergerField()

    def _str_(self):
        return self.name

# many to one for users
class User_Coffe(models.Model):
    name = name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cof_type = models.CharField('type', max_length=1, choices=TYPES, default=MEALS[0][0])
    categories = models.CharField('categories', max_length=1, choices=CATEGORIES, default=MEALS[0][0])
    photo = models.ImageField(upload_to='coffe')

    def _str_(self):
        return self.name







