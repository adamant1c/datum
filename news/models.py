from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class News(models.Model):
    titolo=models.CharField(max_length=22)
    data = models.DateTimeField(auto_now_add=True)
    descrizione=models.TextField(blank=True, null=True)
    user_nutrizionista = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="publisher"
    )
    
    
    img = models.ImageField(blank=True, null=True,upload_to='images_uploaded',validators=[FileExtensionValidator(allowed_extensions=['jpg','png','bmp'])])
    video = models.FileField(blank=True, null=True,upload_to='videos_uploaded',validators=[FileExtensionValidator(allowed_extensions=['mov','avi','mp4','webm','mkv'])])
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
      return reverse("homepage")
    
    def get_number_of_comm_in_news(self):
        """Restituisce il numero di post totali presenti in una istanza di sezione"""
        return Commenti.objects.filter(news=self).count()
    
    def get_n_pages(self):
        """
        Restituisce il numero di pagina presenti in una istanza di Discussione.
        math.ceil https://docs.python.org/3.6/library/math.html#math.ceil
        restituisce il numero intero successivo al float passato come parametro (es 3.1 ==> 4)
        o restituisce lo stesso numero se intero
        """
        posts_news = self.get_number_of_comm_in_news()
        n_pagine = math.ceil(posts_news / 5)
        return n_pagine
    

class Commenti(models.Model):
    
    data = models.DateTimeField(auto_now_add=True)#la data di creazione viene settata quando stiamo creando l'istanza
    titolo = models.CharField(max_length=22)
    descrizione=models.TextField()
    autore= models.CharField(max_length=22,blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Commento"
        verbose_name_plural = "Commenti"

    def __str__(self):
        return self.titolo
