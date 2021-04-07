from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Admin_Coffee, User_Coffee, Reviews, Profile
import boto3
import uuid
import requests
import os

S3_BASE_URL = "https://s3.us-east-2.amazonaws.com/"
BUCKET = "buzzcollector"

# add a photo
def add_photo(photo_file):
    # photo-file will be the "name" attribute on the <input type="file">
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            return url
        except:
            print('An error occurred uploading file to S3')


url = 'https://api.yelp.com/v3'
API = os.environ['API_KEY']
headers = {'Authorization': f'Bearer {API} '}


#r = requests.get(https://api.yelp.com/v3/autocomplete?text=del&latitude=37.786882&longitude=-122.399972, headers=headers)

# home page
def home(request):
    return render(request, 'home.html')

# index store
def store_index(request):
    r = requests.get("https://api.yelp.com/v3/businesses/search?location=toronto&term=coffee&limit=50", headers=headers).json()

    return render(request, 'coffee/store_index.html', {"store": r})

# sign up function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(
                user = user
            )
            return redirect('/search')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# index coffe page
def coffee_index(request):
    coffee = Admin_Coffee.objects.all()
    return render(request, 'coffee/index.html', {'coffee':coffee})

# create coffee form
def coffee_create(request):
    if request.method == 'POST':
        User_Coffee.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            Store_id = request.POST['store'],
            categories = request.POST['categories'],
            # photo = add_photo(request.FILES.get('photo-file', None)),
            profile = Profile.objects.get(user_id=request.user.id)
        )
        return redirect('/profile')
    else:
        return render(request, 'coffee/add_coffee.html')

#view profile
def profile(request):
    return render(request, 'user/profile.html')

# search page
def search(request):
    return render(request, 'main_app/search.html')

# view favorites
def index_favorites(request):
    return render(request, 'user/index_user.html')

# top coffee
def index_top_drinks(request):
    return render(request, 'main_app/search_results.html')

# top store
def index_top_shops(request):
    r = requests.get("https://api.yelp.com/v3/businesses/search?location=toronto&sort_by=rating&categories=coffee&limit=50", headers=headers).json()
    print(r)
    return render(request, 'main_app/search_results.html', {'categories': r})

# type coffee
def index_type_cof(request):
    coffee = User_Coffee.objects.all()
    return render(request, 'main_app/coffee_results.html', {"coffee": coffee})

# type iced coffee
def index_type_ice(request):
    return render(request, 'main_app/search_results.html')

# type Espresso
def index_type_esp(request):
    return render(request, 'main_app/search_results.html')

# type Cappucino
def index_type_cap(request):
    return render(request, 'main_app/search_results.html')
