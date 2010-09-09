from django.contrib import admin
from newblog.posts.models import Post, Etiqueta, Comentario

admin.site.register(Post)
admin.site.register(Etiqueta)
admin.site.register(Comentario)

