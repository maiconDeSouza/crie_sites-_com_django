from django.shortcuts import render
from .models import Post
from django.utils.text import Truncator
# Create your views here.


def home(request):
    posts = Post.objects.all()
    new_posts = [{'id': post.pk, 'autor': post.autor, 'titulo': post.titulo, 'resumo': Truncator(
        post.conteudo).words(30, truncate='...')} for post in posts]

    context = {
        'posts': new_posts
    }
    return render(request, 'blog/home.html', context)


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_details.html', context)
