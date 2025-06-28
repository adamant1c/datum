from django.urls import path

from . import views

urlpatterns = [
        path(
        "vedi-diete/<int:pk>/",
        views.visualizza_dieta,
        name="vedi_diete_cliente",
    ),
      path(
        "vedi-diete/<int:pk>/aggiungi/",
        views.aggiungi_dieta,
        name="aggiungi_una_dieta",
    ),
    path(
        "compila-dieta/<int:pk>/compila/",
        views.compila_dieta,
        name="compila_dieta",
    ),
     path(
        "compila-dieta/<int:pk>/aggiungi/",
        views.aggiungi_pasto,
        name="compila_una_dieta",
    ),
]