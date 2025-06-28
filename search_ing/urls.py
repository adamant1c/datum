from django.urls import path

from . import views

urlpatterns = [
        path(
        "cerca_ingrediente/ricerca",
        views.SearchResultsView .as_view(),
        name="search_results",
    ),
     path(
        "cerca_ingrediente/",
        views.cerca_ingrediente,
        name="Cerca_ingrediente_cliente",
    ),
    
     path("nuovo_ingrediente/", 
        views.CreaIngrediente.as_view(), 
        name="crea_ingrediente"
    ),
    #path("login-user", views.loginpage, name="loginpage"),
    path("vedi_ingredienti", views.VediIngrediente.as_view(), name="homepage"),
    path(
        "elimina_ingrediente/<int:pk>/",
        views.CancellaIngrediente.as_view(),
        name="cancella_ingrediente",
    ),
]