from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost
# Create your views here.

def index(request):
    myposts = blogPost.objects.all()
    return render(request, 'blog/index.html', {'myposts' : myposts})   # render takes two arguments,(request, html file path)

def blogpost(request, id):
    post  = blogPost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {'post' : post})   # render takes two arguments,(request, html file path)
    # third argument post is used to send the data to templates