from django.shortcuts import render
from .models import Post

def puberdademasculina (request):
    return render(request, 'puberdademasculina.html')

def index (request):
    posts = Post.objects.all()
    print(posts)
    context = {
        "posts" : posts,
    }
    return render(request, 'index.html', context)