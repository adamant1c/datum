from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def homepage (request):

    messages.add_message(request, messages.INFO, 'Nuovo Libro!')
    
    return render(request,'home/homepage.html')
    

def profilo (request):
    #messages.add_message(request, messages.INFO, 'Eccoci qui.')
    
    return render(request,'home/profilo_utente.html')
    
    
def servizi (request):
    #messages.add_message(request, messages.INFO, 'Eccoci qui.')
    
    return render(request,'home/servizi.html')

    
    
    
def contatti (request):
    #messages.add_message(request, messages.INFO, 'Eccoci qui.')
    
    return render(request,'home/contatti.html')