from django import forms 
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class PostAddForm(forms.ModelForm):
    # Форма для добавление статьи от пользователя
    
    
    class Meta:
        # поведенческий характер, чертеж для класса
        model = Post
        fields = ('title', 'content', 'photo', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        


class LoginForm(AuthenticationForm):    
    # форма для аутентификации пользователя
    username = forms.CharField(label='Имя пользователя', 
                            max_length=150, 
                            widjet=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', 
                            widjet=forms.PasswordInput(attrs={'class': 'form-control'}))