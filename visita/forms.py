from django import forms
from cliente.models import Visita


#classe meta che ci consente di specificare dei valori che altrimenti avremmo dovuto specificare nel metodo costruttore  init
class VisitaModelForm(forms.ModelForm):
#l'intento dei model form è quello di permetterci di utilizzare i campi dei modelli che vogliamo utilizzare nei nostri form, per questo motivo andiamo a specificare delle caratteristiche aggiuntive
#per ciscun singolo campo che volgiamo personalizzare all'interno della classe meta
    class Meta:
        model = Visita
        fields = ["argomento","descrizione",]
        widgets = {
            "argomento": forms.TextInput(attrs={"placeholder": "Inserire l'argomento della visita", "required":"True"}) ,
            "descrizione": forms.Textarea(attrs={"rows": "10","placeholder": "Inserire i dettagli della visita (e.g. esami, diagnosi) ", "required":"True"}),
        }
        labels = {
            'argomento': 'Titolo',
            'descrizione': 'Dettagli Visita',
        }
        
        
      