from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from newblog.posts.forms import PostForm

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
