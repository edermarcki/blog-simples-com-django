from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Contact


# Create your views here.
def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Banco de Dados',
    'HTML', 'Linux', 'UWSGI', 'Nginx', 'Systemctl']
    list_posts = Post.objects.filter(deleted=False)
    
    data = {'name': 'Curso de Django 3',
    'lista_tecnologias': lista,
    'posts': list_posts}
    
    
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name= name,
        email= request.POST['email'],
        message= request.POST['message']
    )
    return render(request, 'contact_sucess.html',
    {'name_contact': name})