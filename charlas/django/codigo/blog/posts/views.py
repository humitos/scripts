from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from blog.posts.models import PostForm, Post

def agregar_post(request):
    if request.method == 'GET':
        formulario = PostForm()
        return render_to_response('agregar_post.html', {'formulario': formulario})
    else:
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/index')

def index(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render_to_response('index.html', {'posts': posts})


