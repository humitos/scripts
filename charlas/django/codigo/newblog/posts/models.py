from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    etiquetas = models.ManyToManyField('Etiqueta')

    def __unicode__(self):
        return self.titulo

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=25)

    def __unicode__(self):
        return self.nombre

class Comentario(models.Model):
    autor = models.CharField(max_length=25)
    contenido = models.TextField()
    post = models.ForeignKey(Post)
