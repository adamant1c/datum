from django.contrib import admin
from .models import Cliente, Visita



class ClienteModelAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ["nome", "cognome","numero_telefono","email"]
    search_fields = ["cognome"]
    list_filter = ["nome"]


class VisitaModelAdmin(admin.ModelAdmin):
    model = Visita
    list_display = ["argomento", "cliente"]
    search_fields = ["data"]
    list_filter = ["cliente"]




admin.site.register(Cliente, ClienteModelAdmin)
admin.site.register(Visita, VisitaModelAdmin)
