from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/inicio.html')


def recipe(request):
    return render(request, 'blog/receita.html')


def categories(request):
    return render(request, 'blog/categories.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
