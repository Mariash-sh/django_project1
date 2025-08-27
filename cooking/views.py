from django.shortcuts import render
from .models import Category, Post


# Create your views here.
def index(request):
    # Для главной страницы
    posts = Post.objects.all()     #   =Список 
    context = {
        'title': 'Главная страница',
        'posts': posts
    }
    return render(request, 'cooking/index.html', context)
    