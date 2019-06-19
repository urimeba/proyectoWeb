from django import forms
from Apps.Categorias import models as models_categorias
from Apps.Colonias import models as models_colonias
from Apps.Publicaciones import models as models_publicaciones

class ActualizarDatos(forms.Form):
    # PASSWORD, FIRST_NAME, LAST_NAME, EMAIL, 
    colo = models_colonias.Colonias.objects.all()
    CHOICES = tuple((o.pk, o.nombre) for o in colo) 


    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Nombre:', 'name':'nombre','minlength':'5'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Apellido(s):', 'name':'apellido','minlength':'5'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form__input', 'placeholder':'Correo:', 'name':'correo'}))
    contraseña = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'form__input', 'placeholder':'Nueva contraseña', 'name':'contraseña','minlength':'5'}))
    contraseña2 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'form__input', 'placeholder':'Confirma tu contraseña', 'name':'contraseña2','minlength':'5'}))
    
    colonia = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form__input', 'placeholder':'Colonia', 'name':'colonia'}))