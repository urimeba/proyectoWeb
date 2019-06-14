from django import forms
from Apps.Categorias import models as models_categorias
from Apps.Publicaciones import models as models_publicaciones

class PublicacionFormulario(forms.Form):
    cate = models_categorias.Categorias.objects.all()
    CHOICES = tuple((o.pk, o.nombreCategoria) for o in cate) 
       
    titulo =   forms.CharField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Titulo'}))
    descripcion =   forms.CharField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Descripcion'}))
    categoria = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form__input', 'placeholder':'Categoria'}))