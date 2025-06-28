from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from cliente.models import Cliente
from .models import Tipo_pasto, Giorno_settimana, Dieta,Piatti,Ingrediente,Tipo_Pasto_Piatto
from .forms import DietaModelForm,CompilaModelForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic.edit import  DeleteView
# Create your views here.

@login_required
def aggiungi_dieta(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = DietaModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.cliente_dieta = cliente
            form.save()

            url_dieta = reverse("vedi_diete_cliente", kwargs={"pk": pk})
           
            return HttpResponseRedirect(url_dieta)
    else:
        return HttpResponseBadRequest()

@login_required
def visualizza_dieta(request, pk):
    """
    link: https://docs.djangoproject.com/en/dev/topics/pagination/
    """
    cliente_obj = get_object_or_404(Cliente, pk=pk)
    
    lista_diete= Dieta.objects.filter(cliente_dieta=cliente_obj).order_by("nome_dieta")

    paginator = Paginator(lista_diete, 5)
    page = request.GET.get("pagina")
    diete = paginator.get_page(page)

    form_risposta = DietaModelForm()
    context = {
        "cliente": cliente_obj,
        "diete_lista": diete,
        "form_risposta": form_risposta,
    }
    return render(request, "dieta/visualizza_diete.html", context)
    
    
@login_required
def compila_dieta(request, pk):
    """
    # link: https://docs.djangoproject.com/en/dev/topics/pagination/
    # """
    dieta_obj = get_object_or_404(Dieta, pk=pk)
    
    queryset_tipo_pasto= Tipo_Pasto_Piatto.objects.filter(dieta=dieta_obj)
    paginator = Paginator( queryset_tipo_pasto, 2)
    page = request.GET.get("pagina")
    pasti = paginator.get_page(page)
   
    #tipo_pasto_piatto_obj=Tipo_Pasto_Piatto.objects.get(dieta.id==dieta_obj.pk)
   
    form_compila = CompilaModelForm()
    context = {
        
        "tipo_pasto": pasti,
        "form_risposta": form_compila,
        "dieta": dieta_obj,
    }
    print(context)
    return render(request, "dieta/compila_dieta.html", context)
    #return render(request, "dieta/compila_dieta.html")
    
    
@login_required
def aggiungi_pasto(request, pk):
    dieta_obj = get_object_or_404(Dieta, pk=pk)
    #tipo_pasto_piatto_obj= get_object_or_404(Tipo_Pasto_Piatto, dieta.pk==pk)
    if request.method == "POST":
        form = CompilaModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.dieta = dieta_obj
            form.save()

            url_dieta = reverse("compila_dieta", kwargs={"pk": pk})
           
            return HttpResponseRedirect(url_dieta)
    else:
        return HttpResponseBadRequest()