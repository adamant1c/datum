from django import forms
from dieta.models import Ingrediente


#classe meta che ci consente di specificare dei valori che altrimenti avremmo dovuto specificare nel metodo costruttore  init
class IngredienteModelForm(forms.ModelForm):
#l'intento dei model form è quello di permetterci di utilizzare i campi dei modelli che vogliamo utilizzare nei nostri form, per questo motivo andiamo a specificare delle caratteristiche aggiuntive
#per ciscun singolo campo che volgiamo personalizzare all'interno della classe meta
    class Meta:
        model = Ingrediente
        fields = ("Nome","Flag_istamina","Flag_nichel","Flag_ferro","Note")
        widgets = {
            "Nome": forms.TextInput(attrs={"placeholder": "Inserire il nome dell'ingrediente", "required":"True"}) ,
            "Flag_istamina": forms.CheckboxInput(attrs={"placeholder": "Inserire il cognome del cliente", "required":"True"}) ,
            "Flag_nichel": forms.CheckboxInput(attrs={"placeholder": "Inserire il numero di telefono del cliente"}) ,
            "Flag_ferro": forms.CheckboxInput(attrs={"placeholder": "Inserire l'indirizzo del cliente", "required":"True"}) ,
            "Note": forms.Textarea(attrs={"placeholder": "Inserire delle note", "required":"False"}) ,
          
        }
        labels = {
            'nome': 'Nome',
            'Flag_istamina': 'Contiene Istamina?',
            'Flag_nichel': 'Contiene Nichel?',
           'Flag_ferro': 'Contiene Ferro?',
            
        }
        
        