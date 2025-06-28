from django.urls import path

from . import views

urlpatterns = [
        path(
        "vedi-news/",
        views.visualizza_news,
        name="Vai_news",
    ),
      path(
        "vedi-news/aggiungi/",
        views.aggiungi_news,
        name="aggiungi_news",
    ),
    
]