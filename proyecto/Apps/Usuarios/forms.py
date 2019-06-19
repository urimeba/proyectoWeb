from django import forms
from Apps.Categorias import models as models_categorias
from Apps.Colonias import models as models_colonias
from Apps.Publicaciones import models as models_publicaciones

class ActualizarDatos(forms.Form):
    # PASSWORD, FIRST_NAME, LAST_NAME, EMAIL, 
    colo = models_colonias.Colonias.objects.all()
    CHOICES = tuple((o.pk, o.nombre) for o in colo) 


    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Nombre:', 'name':'nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Apellido(s):', 'name':'apellido'}))
    correo = forms.EmailField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Correo:', 'name':'correo'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form__input', 'placeholder':'Apellido(s):', 'name':'contraseña'}))
       
    colonia = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form__input', 'placeholder':'Colonia', 'name':'colonia'}))