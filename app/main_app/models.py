from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CATEGORIES = (
    ('CE', 'Coffee'),
    ('IC', 'Iced Coffee'),
    ('E', 'Espresso'),
    ('CA', 'Cappucino'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, default=0)
    avatar = models.CharField(max_length=200)

# many to one for users 
class Admin_Coffee(models.Model):
    name = models.CharField(max_length=50)
    store_id = models.CharField('Store name',max_length=50)
    categories = models.CharField('Categories', max_length=(20))
    photo = models.CharField(max_length=200, default='https://i.imgur.com/DXtLJUo.png')
    rating = models.FloatField(default=0)
    profile = models.ForeignKey(Profile,related_name='usersubad', on_delete=models.CASCADE, default=0)
    favorite_count = models.IntegerField(default=0)
    favorites = models.ManyToManyField(Profile)

    def _str_(self):
        return self.name

# many to one for users
class User_Coffee(models.Model):
    name = models.CharField(max_length=50)
    store_id = models.CharField('Store name',max_length=50)
    categories = models.CharField('Categories', max_length=(2), choices=(CATEGORIES), default=CATEGORIES[0][0])
    photo = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, related_name='usersub', on_delete=models.CASCADE, default=0)

    def _str_(self):
        return self.name

# many to one for users and coffee
class Reviews(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=0)
    review = models.CharField( max_length=1000)
    rating = models.CharField(
        'Rating', 
        max_length=(1), 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    coffee = models.ForeignKey(Admin_Coffee, on_delete=models.CASCADE)

    def _str_(self):
        return "%S %S" % (self.profile.user.username, self.coffee.name)
