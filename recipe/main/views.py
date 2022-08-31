from django.shortcuts import render
from django.contrib.auth.models import User
from  django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':recipes})

def about(request):
    return render(request, 'about.html')

def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user':user})

class RecipeDetail(DetailView):
    model = Recipe

class RecipeDelete(DetailView):
    model = Recipe
    success_url = 'home'

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.owner

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['name', 'description', 'price', 'image']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.owner

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'description', 'price', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


