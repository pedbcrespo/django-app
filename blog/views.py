from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import datetime

def home(request):
    now = datetime.datetime.now()
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/home.html',{'posts':posts})

def fotos(request):

    return render(request, 'blog/fotos.html',{})