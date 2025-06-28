from django import forms
from .models import Cliente


#classe meta che ci consente di specificare dei valori che altrimenti avremmo dovuto specificare nel metodo costruttore  init
class ClienteModelForm(forms.ModelForm):
#l'intento dei model form è quello di permetterci di utilizzare i campi dei modelli che vogliamo utilizzare nei nostri form, per questo motivo andiamo a specificare delle caratteristiche aggiuntive
#per ciscun singolo campo che volgiamo personalizzare all'interno della classe meta
    class Meta:
        model = Cliente
        fields = ["nome","cognome","numero_telefono","indirizzo","email","patologia"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Inserire il nome del cliente", "required":"True"}) ,
            "cognome": forms.TextInput(attrs={"placeholder": "Inserire il cognome del cliente", "required":"True"}) ,
            "numero_telefono": forms.TextInput(attrs={"placeholder": "Inserire il numero di telefono del cliente"}) ,
            "indirizzo": forms.TextInput(attrs={"placeholder": "Inserire l'indirizzo del cliente", "required":"True"}) ,
            "email": forms.TextInput(attrs={"placeholder": "Inserire la mail del cliente", "required":"True"}) ,
            "patologia": forms.Textarea(attrs={"rows": "4","placeholder": "Inserire la diagnosi"}),
        }
        labels = {
            'nome': 'Nome',
            'cognome': 'Cognome',
            'numero_telefono': 'Numero di Telefono',
            'indirizzo': 'Indirizzo',
            'email': 'Email',
            'argomento': 'Titolo',
            'patologia': 'Patologia',
        }
        
        