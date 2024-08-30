from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    cadegoria = models.CharField(max_length=40)
    descricao = models.TextField(max_length=300)
    foto = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo