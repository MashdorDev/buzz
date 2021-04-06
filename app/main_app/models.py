from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
    ('C', 'Coffee'),
    ('IC', 'Iced Coffee'),
    ('E', 'Espresso'),
    ('C', 'Cappucino'),
)

RATING = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)

# many to one for users 
class Admin_Coffee(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Store_id = models.CharField('Store name',max_length=50)
    categories = models.CharField('Categories', max_length=(2), choices=(CATEGORIES), default=CATEGORIES[0][0])
    # photo = models.ImageField(upload_to='coffee')
    rating = models.IntegerField()
    user = models.ForeignKey(User,related_name='usersubad', on_delete=models.CASCADE, default=0)
    favorite_count = models.IntegerField()
    favorites = models.ManyToManyField(User)

    def _str_(self):
        return self.name

# many to one for users
class User_Coffee(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Store_id = models.CharField('Store name',max_length=50)
    categories = models.CharField('Categories', max_length=(2), choices=(CATEGORIES), default=CATEGORIES[0][0])
    # photo = models.ImageField(upload_to='coffee')
    user = models.ForeignKey(User, related_name='usersub', on_delete=models.CASCADE, default=0)

    def _str_(self):
        return self.name

# many to one for users and coffee
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    review = models.CharField( max_length=1000)
    rating = models.CharField('Rating', max_length=(1), choices=(RATING), default=RATING[0][0])
    coffee = models.ForeignKey(Admin_Coffee, on_delete=models.CASCADE)

    def _str_(self):
        return "%S %S" % (self.user.username, self.coffee.name)
