from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('receita/', views.recipe, name='receita'),
    path('categorias/', views.categories, name='categorias'),
    path('sobre/', views.about, name='sobre'),
    path('contato/', views.contact, name='contato'),
]
