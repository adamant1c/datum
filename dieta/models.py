from django.db import models
from cliente.models import Cliente
# Create your models here.


class Ingrediente(models.Model):
  Nome = models.CharField(max_length=22)
  Flag_istamina=models.BooleanField(null=True)
  Flag_nichel=models.BooleanField(null=True)
  Flag_ferro=models.BooleanField(null=True)
  Note=models.TextField(blank=True, null=True)
  
  class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredienti"
        ordering=['Nome']
        
  def __str__(self):
        return self.Nome

class Piatti(models.Model):
    nome_piatto=models.CharField(max_length=30)
    costo_preparazione = models.IntegerField(blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    descrizione=models.TextField(blank=True, null=True)
    tempo_preparazione = models.IntegerField(blank=True, null=True)
    tempo_cottura = models.IntegerField(blank=True, null=True)
    ricetta=models.TextField(blank=True, null=True)
    Calorie_kcal=models.FloatField(blank=True, null=True)
    Carboidrati_g=models.FloatField(blank=True, null=True)
    Zuccheri_g=models.FloatField(blank=True, null=True)
    Grassi_g=models.FloatField(blank=True, null=True)
    Grassi_Saturi_g=models.FloatField(blank=True, null=True)
    Fibre_g=models.FloatField(blank=True, null=True)
    Colesterolo_m=models.FloatField(blank=True, null=True)
    Sodio_mg=models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Piatto"
        verbose_name_plural = "Piatti"

    def __str__(self):
        return self.nome_piatto

class Tipo_pasto(models.Model):
  tipo = models.CharField(max_length=10)
  
  class Meta:
        verbose_name = "Tipo di pasto"
        verbose_name_plural = "Tipi di pasto"
        
  def __str__(self):
        return self.tipo

class Ingrediente_Piatto(models.Model):
  Nome = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
  Metodo_Preparazione = models.CharField(max_length=22,blank=True, null=True)
  Quantità = models.FloatField()
  UM=models.TextField(max_length=5,blank=True, null=True)
  Piatto=models.ForeignKey(Piatti, on_delete=models.CASCADE, null=True)
  
  
  
  class Meta:
        verbose_name = "Ingrediente nel piatto"
        verbose_name_plural = "Ingredienti nei piatti"
        ordering=['Nome']
        
  def __str__(self):
        return self.Nome.Nome + self.Piatto.nome_piatto




    
class Giorno_settimana(models.Model):
  giorno = models.CharField(max_length=10)
  class Meta:
        verbose_name = "Giorno della settimana"
        verbose_name_plural = "Giorni della settimana"
        
  def __str__(self):
        return self.giorno


        

    
class Dieta(models.Model):
    data = models.DateTimeField(auto_now_add=True, null=True)
    nome_dieta=models.CharField(max_length=22)
    descrizione=models.TextField(blank=True, null=True)
    cliente_dieta= models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Dieta"
        verbose_name_plural = "Diete"
        ordering=['-data','nome_dieta']
        
    def __str__(self):
        return self.nome_dieta

class Tipo_Pasto_Piatto(models.Model):
    tipo_pasto = models.ManyToManyField(Tipo_pasto)
    giorno_settimana = models.ManyToManyField(Giorno_settimana)
    dieta=  models.ForeignKey(Dieta, on_delete=models.CASCADE)
    nome_piatto=models.ForeignKey(Piatti, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Pasto vs Dieta"
        verbose_name_plural = "Pasti vs Diete"

    def __str__(self):
        return self.dieta.nome_dieta + " " +  self.nome_piatto.nome_piatto
