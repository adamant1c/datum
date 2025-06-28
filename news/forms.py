from django import forms
from .models import News


#classe meta che ci consente di specificare dei valori che altrimenti avremmo dovuto specificare nel metodo costruttore  init
class NewsModelForm(forms.ModelForm):
#l'intento dei model form è quello di permetterci di utilizzare i campi dei modelli che vogliamo utilizzare nei nostri form, per questo motivo andiamo a specificare delle caratteristiche aggiuntive
#per ciscun singolo campo che volgiamo personalizzare all'interno della classe meta
    class Meta:
        model = News
        fields = ["titolo","descrizione","img","video"]
        widgets = {
            "titolo": forms.TextInput(attrs={"placeholder": "Inserire il titolo della Novità", "required":"True"}) ,
            "descrizione": forms.Textarea(attrs={"rows": "10","placeholder": "Inserire i dettagli della Novità", "required":"False"}),
            "img": forms.ClearableFileInput(attrs={"required":"False"}),
            "video": forms.ClearableFileInput(attrs={"required":"False"}),
        }
        labels = {
            'titolo': 'Titolo',
            'descrizione': 'Dettagli',
             'img': 'Carica immagine',
              'video': 'Carica video',
        }
        
        
      