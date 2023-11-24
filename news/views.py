from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

# Create your views here.



def home(request):
    posts = Post.objects.all()
    return render(request, 'homepage.html', {'posts': posts})

def post_details(request,id):
    return render(request, 'details.html' ,{'id': id})

def global_news(request):
    return render(request, 'grobal_news.html')