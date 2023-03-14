from django.shortcuts import render

from .models import Post

# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/inicio.html', context)


def recipe(request, pk):
    return render(request, 'blog/receita.html')


def categories(request):
    return render(request, 'blog/categories.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
