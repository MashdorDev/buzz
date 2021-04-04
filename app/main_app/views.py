from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Admin_Coffee, User_Coffee, Favorites, Reviews


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

# sign up function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
