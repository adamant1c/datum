from django.contrib import admin
from .models import Tipo_pasto, Giorno_settimana, Dieta,Piatti,Ingrediente,Ingrediente_Piatto,Tipo_Pasto_Piatto

class  Tipo_Pasto_PiattoModelAdmin(admin.ModelAdmin):
    model = Tipo_Pasto_Piatto
    list_display = ["nome_piatto","dieta"]
    search_fields = ["giorno_settimana","tipo_pasto"]
    list_filter = ["dieta","nome_piatto"]



class Ingrediente_PiattoModelAdmin(admin.ModelAdmin):
    model = Ingrediente_Piatto
    list_display = ["Nome","Quantità","Metodo_Preparazione","UM","Piatto"]
    search_fields = ["Quantità"]
    list_filter = ["Nome"]
    
class IngredienteModelAdmin(admin.ModelAdmin):
    model = Ingrediente
    list_display = ["Nome","Note"]
    search_fields = ["Flag_istamina","Flag_nichel","Flag_ferro"]


class Tipo_pastoModelAdmin(admin.ModelAdmin):
    model = Tipo_pasto
    list_display = ["tipo"]
    search_fields = ["tipo"]
    

class Giorno_settimanaModelAdmin(admin.ModelAdmin):
    model = Giorno_settimana
    list_display = ["giorno"]
    search_fields = ["giorno"]


class DietaModelAdmin(admin.ModelAdmin):
    model = Dieta
    list_display = ["nome_dieta", "descrizione","cliente_dieta"]
    search_fields = ["nome_dieta"]
    list_filter = ["cliente_dieta"]



class PiattoModelAdmin(admin.ModelAdmin):
    model = Piatti
    list_display = ["nome_piatto", "descrizione"]
    search_fields = ["tempo_preparazione","tempo_cottura"]
    list_filter = ["categoria","costo_preparazione"]

    
admin.site.register(Tipo_Pasto_Piatto, Tipo_Pasto_PiattoModelAdmin)    
admin.site.register(Ingrediente_Piatto, Ingrediente_PiattoModelAdmin)
admin.site.register(Ingrediente, IngredienteModelAdmin)
admin.site.register(Tipo_pasto, Tipo_pastoModelAdmin)
admin.site.register(Giorno_settimana, Giorno_settimanaModelAdmin)
admin.site.register(Dieta, DietaModelAdmin)
admin.site.register(Piatti, PiattoModelAdmin)