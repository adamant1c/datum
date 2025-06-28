from django.urls import path

from . import views

urlpatterns = [
    path("nuovo-cliente/", 
        views.CreaCliente.as_view(), 
        name="crea_cliente"
    ),
    #path("login-user", views.loginpage, name="loginpage"),
    path("homepage", views.HomeVista.as_view(), name="homepage"),
    path(
        "cliente/elimina-cliente/<int:pk>/",
        views.CancellaCliente.as_view(),
        name="cancella_cliente",
    ),
]
