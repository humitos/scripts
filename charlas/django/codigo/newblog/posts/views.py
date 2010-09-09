from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from newblog.posts.forms import PostForm
from newblog.posts.models import Post

def agregar_post(request):
    if request.method == 'GET':
        formulario = PostForm()
        return render_to_response('posts/agregar_post.html',
                                 {'formulario': formulario})
    else:
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/')

def index(request):
    posts = Post.objects.all()

    return render_to_response('index.html',
                              {'posts': posts,
                               'variable': 'una cadena'})
