from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm, LoginForm
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    # Для главной страницы
    posts = Post.objects.all()     #   =Список 
    context = {
        'title': 'Главная страница',
        'posts': posts,
    }
    return render(request, 'cooking/index.html', context)
    
    
def category_list(request, pk):
    # реакция на нажатие кнопочек
    posts = Post.objects.filter(category_id=pk)    #   =Список 
    context = {
        'title': posts[0].category,
        'posts': posts,
        
    }
    return render(request, 'cooking/index.html', context)



def post_detail(request, pk):
    # Страничка статьи
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
    ext_posts = Post.objects.all().order_by('-watched')[:5]
    context = {
        'title': article.title,
        'post': article,
        'ext_posts': ext_posts,
    }
    
    return render(request, 'cooking/arcticle_detail.html', context)


def add_post(request):
    # Добавление статьи от пользователя, без админки
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostAddForm()
        
    context = {
        'form': form,
        'title': 'Добавить статью',
    }
    return render(request, 'cooking/article_add_form.html', context)



def user_login(request):
    # Аутентификация пользователя
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'title': 'Добавить статью',
    }           