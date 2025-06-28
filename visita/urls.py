from django.urls import path

from . import views

urlpatterns = [
        path(
        "vedi-visite/<int:pk>/",
        views.visualizza_visita,
        name="vedi_visite_cliente",
    ),
      path(
        "vedi-visite/<int:pk>/aggiungi/",
        views.aggiungi_visita,
        name="aggiungi_una_visita",
    ),
    
]