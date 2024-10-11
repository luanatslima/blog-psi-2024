from django.shortcuts import render
from .models import Post

def puberdademasculina (request):
    lista_caracteristicas = [
        {}
    ]
    context = {
        "caracteristicas" : lista_caracteristicas,
    }
    return render(request, 'puberdademasculina.html', context)

def index (request):
    posts = Post.objects.all()
    print(posts)
    context = {
        "posts" : posts,
    }
    return render(request, 'index.html', context)