from django.shortcuts import render
from django.urls import reverse_lazy

from dieta.models import Ingrediente
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Q
from .forms import IngredienteModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def cerca_ingrediente (request):

    
    
    return render(request,'search_ing/cerca_ingrediente.html')
    

class SearchResultsView(ListView):
    model = Ingrediente
    template_name = 'search_ing/risultato_ricerca.html'

    def get_queryset(self): # new
     
        query = self.request.GET.get('q')
        object_list = Ingrediente.objects.filter(
            Q(Nome__icontains=query) | Q(Note__icontains=query)
        )
        return object_list
        


        
class CreaIngrediente(CreateView):
    model = Ingrediente
    fields = ("Nome","Flag_istamina","Flag_nichel","Flag_ferro","Note")
    template_name = "search_ing/crea_ingrediente.html"
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        
        form.instance.user_cliente = self.request.user
        
        return super(CreaIngrediente, self).form_valid(form)
        
        
#@login_required
class VediIngrediente(LoginRequiredMixin,ListView):
    # discussione = get_object_or_404(Discussione, pk=pk)
    # posts_discussione = Post.objects.filter(discussione=discussione)
    # queryset = Cliente.objects.filter( user_cliente=user)
    template_name = 'search_ing/visualizza_ingredienti.html'
    context_object_name = "lista_ingredienti"
    
    def get_queryset(self):
        return Ingrediente.objects.all()
        
        
class CancellaIngrediente(DeleteView):
    model = Ingrediente
    #success_url = "/forum/casa/"+self.id
    success_url = "search_ing/visualizza_ingredienti.html"