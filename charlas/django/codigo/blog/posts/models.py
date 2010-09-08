from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=25)

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta)

class Comentario(models.Model):
    autor = models.CharField(max_length=25)
    contenido = models.TextField()
    post = models.ForeignKey(Post)

# Formularios
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post

