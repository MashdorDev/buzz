from django.db import models
import os
from django.contrib.auth.models import User

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

# many to one for users 
class Admin_Coffe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cof_type = models.CharField('type', max_length=2, choices=TYPES, default=TYPES[0][0])
    categories = models.CharField('categories', max_length=2, choices=CATEGORIES, default=CATEGORIES[0][0])
    photo = models.ImageField(upload_to='coffe')
    rating = models.IntegerField()
    favorite_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def _str_(self):
        return self.name

# many to one for users
class User_Coffe(models.Model):
    name = name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cof_type = models.CharField('type', max_length=2, choices=TYPES, default=TYPES[0][0])
    categories = models.CharField('categories', max_length=2, choices=CATEGORIES, default=CATEGORIES[0][0])
    photo = models.ImageField(upload_to='coffe')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def _str_(self):
        return self.name

# Tracking user favorites many to one for users and many to many for coffes
class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    coffe = models.ManyToManyField(Admin_Coffe)
    
    def _str_(self):
        return "%S %S" % (self.user.username, self.coffe.name)



# many to one for users and coffee
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    review = models.CharField( max_length=1000)
    rating = models.IntegerField()
    coffe = models.ForeignKey(Admin_Coffe, on_delete=models.CASCADE)

    def _str_(self):
        return "%S %S" % (self.user.username, self.coffe.name)





