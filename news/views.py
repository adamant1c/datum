from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import News,Commenti
from .forms import NewsModelForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic.edit import  DeleteView
from django.urls import reverse
# Create your views here.

@login_required
def aggiungi_news(request):
    
    if request.method == "POST":
        form = NewsModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user_nutrizionista = request.user
            form.save()

            url_news = reverse("Vai_news")
           
            return HttpResponseRedirect(url_news)
    else:
        return HttpResponseBadRequest()


def visualizza_news(request):

   
    lista_news= News.objects.all().order_by("-data")

    paginator = Paginator(lista_news, 5)
    page = request.GET.get("pagina")
    news = paginator.get_page(page)

    form_risposta = NewsModelForm()
    context = {
        "news_lista": news,
        "form_risposta": form_risposta,
    }
    return render(request, "news/visualizza_news.html", context)