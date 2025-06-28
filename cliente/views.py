from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from .models import Cliente
from django.views.generic.edit import CreateView, DeleteView
from .mixins import StaffMixing
from .forms import ClienteModelForm
# Create your views here.

class CreaCliente(CreateView):
    model = Cliente
    fields = ("nome","cognome","numero_telefono","indirizzo","email","patologia")
    template_name = "cliente/crea_cliente.html"
    success_url = "/cliente/homepage"

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user_cliente = self.request.user
        
        return super(CreaCliente, self).form_valid(form)
    
    
def loginpage (request):
    base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return render(request,os.path.join(base_dir,'templates/registration/login.html'))
    #return render(request,'/home/pi/Dat_sc_prj/prg_DV/Patri/templates/registration/login.html')



#@login_required
#def homepage (request):
#    return render(request,'core/homepage.html')

#@login_required
class HomeVista(LoginRequiredMixin,ListView):
    # discussione = get_object_or_404(Discussione, pk=pk)
    # posts_discussione = Post.objects.filter(discussione=discussione)
    # queryset = Cliente.objects.filter( user_cliente=user)
    template_name = 'cliente/homepage.html'
    context_object_name = "lista_clienti"
    
    def get_queryset(self):
        return Cliente.objects.filter(user_cliente=self.request.user)
        
        
class CancellaCliente(DeleteView):
    model = Cliente
    #success_url = "/forum/casa/"+self.id
    success_url = "/cliente/homepage"
    