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


# home page
def home(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'aboutus.html')


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

# Coffee Details
def coffee_detail(request, coff_id):
    coffee = Admin_Coffee.objects.get(id=coff_id)
    rev = Reviews.objects.filter(coffee_id=coff_id)
    store = requests.get("https://api.yelp.com/v3/businesses/"+ coffee.store_id, headers=headers).json()
    return render(request, "coffee/detail.html", {'coffee': coffee, 'store': store, 'reviews': rev})

# Store detail page
def store_details(request, sto_id):
    r = requests.get("https://api.yelp.com/v3/businesses/"+ sto_id, headers=headers).json()
    coffee = Admin_Coffee.objects.filter(store_id=sto_id)
    return render(request, 'coffee/store_index.html', {"store": r, 'coffee':coffee})

# create coffee form
def coffee_create(request, sto_id):
    r = requests.get("https://api.yelp.com/v3/businesses/"+ sto_id, headers=headers).json()
    if request.method == 'POST':
        User_Coffee.objects.create(
            name = request.POST['name'],
            store_id = sto_id,
            categories = request.POST['categories'],
            photo = add_photo(request.FILES.get('photo-file', None)),
            profile = Profile.objects.get(user_id=request.user.id)
        )
        return redirect('/profile')
    else:
        return render(request, 'coffee/add_coffee.html', {'store': r})


# search page
def search(request):
    return render(request, 'main_app/search.html')

def searching(request):
    if request.POST['selector']=='store':
        results = requests.get("https://api.yelp.com/v3/businesses/search?location=toronto&sort_by=rating&categories=coffee&limit=50&term=" + request.POST["search"], headers=headers).json()
        return render(request, 'main_app/search_results.html', {'categories':results})
    else:
        results = Admin_Coffee.objects.filter(name__icontains=request.POST['search'])
        return render(request, 'main_app/coffee_results.html', {'coffee': results})

# view favorites
def index_favorites(request):
    coffee = Admin_Coffee.objects.filter(favorites__id=Profile.objects.get(user_id=request.user.id).id)
    return render(request, 'user/index_favorites.html', {"coffee": coffee})

# add to favorites
def add_favorite(request, coff_id):
    coffee= Admin_Coffee.objects.get(id=coff_id)
    coffee.favorites.add(Profile.objects.get(user_id=request.user.id))
    coffee.favorite_count = coffee.favorite_count + 1
    coffee.save()
    return redirect('/coffee/detail/%s/' % (coff_id))

def delete_favorite(request, coff_id):
    coffee= Admin_Coffee.objects.get(id=coff_id)
    coffee.favorites.remove(Profile.objects.get(user_id=request.user.id))
    coffee.favorite_count = coffee.favorite_count - 1
    coffee.save()
    return redirect('/profile/favorites/')

# top coffee
def index_top_drinks(request):
    coffee = Admin_Coffee.objects.all().order_by('-rating')
    return render(request, 'main_app/coffee_results.html', {"coffee": coffee})

# top store
def index_top_shops(request):
    r = requests.get("https://api.yelp.com/v3/businesses/search?location=toronto&sort_by=rating&categories=coffee&limit=50", headers=headers).json()
    return render(request, 'main_app/search_results.html', {'categories': r})

# type coffee
def index_type_cof(request):
    coffee = Admin_Coffee.objects.filter(categories="C")
    return render(request, 'main_app/coffee_results.html', {"coffee": coffee})

# type iced coffee
def index_type_ice(request):
    coffee = Admin_Coffee.objects.filter(categories="IC")
    return render(request, 'main_app/coffee_results.html', {"coffee": coffee})

# type Espresso
def index_type_esp(request):
    coffee = Admin_Coffee.objects.filter(categories="E")
    return render(request, 'main_app/coffee_results.html', {"coffee": coffee})

# type Cappucino
def index_type_cap(request):
    coffee = Admin_Coffee.objects.filter(categories="C")
    return render(request, 'main_app/coffee_results.html', {"coffee": coffee})

# view profile
def profile(request):
    using = Profile.objects.get(user_id=request.user.id)
    return render(request, 'user/profile.html', {'using':using})

# change avatar image
def create_avatar(request):
    using = Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        using.avatar = add_photo(request.FILES.get('photo-file', None))
        using.save()
        return redirect('/profile')
    else:
        return render(request, 'user/avatar.html', {'using': using})

# view my reviews
def index_review(request):
    mine = Reviews.objects.filter(profile_id=Profile.objects.get(user_id=request.user.id))
    return render(request, 'user/review_index.html', {'mine': mine})

# delete reviews
def delete_review(request, rev_id):
    r = Reviews.objects.get(id=rev_id)
    r.delete()
    return redirect('/profile/review/')

# add a review
def create_review(request, coff_id):
    coffee = Admin_Coffee.objects.get(id=coff_id)
    if request.method == 'POST':
        Reviews.objects.create(
            review = request.POST['review'],
            rating = request.POST['rating'],
            coffee_id = coff_id,
            profile = Profile.objects.get(user_id=request.user.id)
        )
        update = Reviews.objects.filter(coffee_id=coff_id)
        rate = 0
        count = 0
        for i in update:
            count += 1
            rate += int(i.rating)
        coffee.rating = round(rate/count, 1)
        coffee.save()
        return redirect('/coffee/detail/%s/' % (coff_id))
    else:
        return render(request, 'coffee/review.html', {"coffee": coffee })


# view my submissions
def index_submissions(request):
    mine_user = User_Coffee.objects.filter(profile_id=Profile.objects.get(user_id=request.user.id))
    mine_admin = Admin_Coffee.objects.filter(profile_id=Profile.objects.get(user_id=request.user.id))
    return render(request, 'user/submitted_index.html', {'mine_user': mine_user, 'mine_admin': mine_admin})

# adming coffee approval
def admin_approval(request):
    coffee = User_Coffee.objects.all()
    return render(request,'user/admin_approval.html', {'coffee':coffee, "length": len(coffee) - 1})

# admin coffee approved
def approved(request, cof_id):
    c = User_Coffee.objects.get(id=cof_id)
    Admin_Coffee.objects.create(
        name = request.POST['name'],
        store_id = request.POST['store'],
        categories = request.POST['categories'],
        photo = request.POST['photo-file'],
        profile = c.profile
    )
    c.delete()
    return redirect('/approval/admin')

# delete a coffee
def delete_ad(request, cof_id):
    c = User_Coffee.objects.get(id=cof_id)
    c.delete()
    return redirect('/approval/admin')
