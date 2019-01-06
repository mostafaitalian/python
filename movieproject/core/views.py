from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.


class MovieList(ListView):
    model = Movie
    
class MovieDetail(DetailView):
    model = Movie