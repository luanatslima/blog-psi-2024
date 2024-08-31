from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(blank=True)
    texto = models.TextField(max_length=300)

    def __str__(self):
        return self.titulo