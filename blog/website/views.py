from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Banco de Dados',
    'HTML', 'Linux', 'UWSGI', 'Nginx', 'Systemctl']
    list_posts = Post.objects.all()
    
    data = {'name': 'Curso de Django 3',
    'lista_tecnologias': lista,
    'posts': list_posts}
    
    
    return render(request, 'index.html', data)