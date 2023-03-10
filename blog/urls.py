from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('receitas/', views.recipes, name='receitas'),
]
