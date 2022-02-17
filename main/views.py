from msilib.schema import ListView
from tempfile import tempdir
from django.shortcuts import render
from main import models
from django.views.generic import(
    ListView,
    DetailView
)

# Create your views here.

class Index(ListView):
    model=models.Question
    template_name='main/index.html'


class Question(DetailView):
    model=models.Question
    template_name='main\question.html'
