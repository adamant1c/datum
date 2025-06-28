from django import forms
from .models import Dieta,Tipo_Pasto_Piatto


  

#classe meta che ci consente di specificare dei valori che altrimenti avremmo dovuto specificare nel metodo costruttore  init
class DietaModelForm(forms.ModelForm):
#l'intento dei model form è quello di permetterci di utilizzare i campi dei modelli che vogliamo utilizzare nei nostri form, per questo motivo andiamo a specificare delle caratteristiche aggiuntive
#per ciascun singolo campo che volgiamo personalizzare all'interno della classe meta
    class Meta:
        model = Dieta
        fields = ["nome_dieta","descrizione"]
        widgets = {
            "nome_dieta": forms.TextInput(attrs={"placeholder": "Inserire un nome alla dieta", "required":"True"}) ,
            "descrizione": forms.Textarea(attrs={"rows": "10","placeholder": "Inserire i dettagli della dieta "}),
        }
        labels = {
            'nome_dieta': 'Nome',
            'descrizione':'Descrizione'
        }

        

class CompilaModelForm(forms.ModelForm):
# #l'intento dei model form è quello di permetterci di utilizzare i campi dei modelli che vogliamo utilizzare nei nostri form, per questo motivo andiamo a specificare delle caratteristiche aggiuntive
# #per ciascun singolo campo che volgiamo personalizzare all'interno della classe meta
    class Meta:
        model = Tipo_Pasto_Piatto
        fields = ["tipo_pasto","giorno_settimana","nome_piatto"]
        