from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from cliente.models import Cliente,Visita
from .forms import VisitaModelForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic.edit import  DeleteView
# Create your views here.

@login_required
def aggiungi_visita(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = VisitaModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.cliente = cliente
            form.save()

            url_visita = reverse("vedi_visite_cliente", kwargs={"pk": pk})
           
            return HttpResponseRedirect(url_visita)
    else:
        return HttpResponseBadRequest()

@login_required
def visualizza_visita(request, pk):
    """
    link: https://docs.djangoproject.com/en/dev/topics/pagination/
    """
    cliente_obj = get_object_or_404(Cliente, pk=pk)
    print(cliente_obj)
    print(request.user)
    lista_visite= Visita.objects.filter(cliente=cliente_obj).order_by("-data")

    paginator = Paginator(lista_visite, 5)
    page = request.GET.get("pagina")
    visite = paginator.get_page(page)

    form_risposta = VisitaModelForm()
    context = {
        "cliente": cliente_obj,
        "visite_lista": visite,
        "form_risposta": form_risposta,
    }
    return render(request, "visita/visualizza_visite.html", context)