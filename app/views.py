from django.shortcuts import render
from .models import Post
from .models import Topico

def puberdademasculina (request):
    topicos = Topico.objects.all()
    print(topicos)
    context = {
        "topicos": topicos,
    }
    return render(request, 'puberdademasculina.html', context)

def index (request):
    posts = Post.objects.all()
    print(posts)
    context = {
        "posts" : posts,
    }
    return render(request, 'index.html', context)