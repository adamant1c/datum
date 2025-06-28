from django.urls import path,include
from . import views
from news import views as news_view
from search_ing import views as views_ing

urlpatterns = [
    path("profilo/", views.profilo, name="Vai_profilo"),
    path("", views.homepage, name="Homepage"),
    path("servizi/", views.servizi, name="Vai_servizi"),
    path("news/", include('news.urls')),
    path("contatti/", views.contatti, name="Vai_contatti"),
    path(
        "cerca_ingrediente/",
        views_ing.cerca_ingrediente,
        name="Cerca_ingrediente_cliente",
    ),
]
