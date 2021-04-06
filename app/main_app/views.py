from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Admin_Coffee, User_Coffee, Reviews


# home page
def home(request):
    return render(request, 'home.html')



# index coffe page
def coffee_index(request):
    coffee = Admin_Coffee.objects.all()
    return render(request, 'coffee/index.html', {'coffee':coffee})


# create coffee form
class coffee_create( CreateView):
    model = Admin_Coffee
    fields = '__all__'

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)

# index store
def store_index(request):
    return render(request, 'coffee/store_index.html')

# sign up function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/search')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

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
    return render(request, 'main_app/search_results.html')

# type coffee
def index_type_cof(request):
    return render(request, 'main_app/search_results.html')

# type iced coffee
def index_type_ice(request):
    return render(request, 'main_app/search_results.html')

# type Espresso
def index_type_esp(request):
    return render(request, 'main_app/search_results.html')

# type Cappucino
def index_type_cap(request):
    return render(request, 'main_app/search_results.html')