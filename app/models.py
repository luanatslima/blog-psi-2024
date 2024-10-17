from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(blank=True)
    conteudo = models.TextField(max_length=1200)

    def __str__(self):
        return self.titulo

    
class Topico(models.Model):
    titulo = models.CharField(max_length=300)
    foto = models.ImageField(blank=True)
    conteudo = models.TextField(max_length=1200)
    
    def __str__(self):
        return self.titulo