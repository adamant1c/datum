from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import math

# Create your models here.

class Cliente(models.Model):
    nome=models.CharField(max_length=22)
    cognome = models.CharField(max_length=22)
    numero_telefono = models.CharField(max_length=22,blank=True, null=True)
    indirizzo=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=40,blank=True, null=True)
    patologia=models.TextField(blank=True, null=True)
    user_cliente = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="nutrizionista"
    )
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"

    def __str__(self):
        return self.nome+" "+self.cognome

    def get_absolute_url(self):
      return reverse("homepage")
    
    def get_number_of_vis_in_clie(self):
        """Restituisce il numero di post totali presenti in una istanza di sezione"""
        return Visita.objects.filter(cliente=self).count()
    
    def get_n_pages(self):
        """
        Restituisce il numero di pagina presenti in una istanza di Discussione.
        math.ceil https://docs.python.org/3.6/library/math.html#math.ceil
        restituisce il numero intero successivo al float passato come parametro (es 3.1 ==> 4)
        o restituisce lo stesso numero se intero
        """
        posts_visita = self.get_number_of_vis_in_clie()
        n_pagine = math.ceil(posts_visita / 5)
        return n_pagine
    

class Visita(models.Model):
   
    data = models.DateTimeField(auto_now_add=True)#la data di creazione viene settata quando stiamo creando l'istanza
    argomento = models.CharField(max_length=22)
    descrizione=models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visite"

    def __str__(self):
        return self.argomento

