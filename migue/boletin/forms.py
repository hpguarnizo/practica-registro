from django import forms
from .models import Registrado, Info_contacto, Info_acerca
#********************** F O R M U L A R I O S *****************************************************
class RegModelForm(forms.ModelForm):
    class Meta:
        model=Registrado
        fields= ["nombre","email"]

    def clean_email(self):
        email= self.cleaned_data.get("email")
        email_base, proveedor= email.split("@")
        dominio,extension = proveedor.split(".")
        if not extension =="edu":
            raise forms.ValidationError("Coloca Edu")
        return email

    def clean_nombre(self):
        nombre= self.cleaned_data.get("nombre")
        return nombre
    #validaciones

class ContactForm(forms.Form):
        nombre = forms.CharField(required=False)
        email = forms.EmailField()
        mensaje= forms.CharField(widget=forms.Textarea)

class Acercaform(forms.Form):

    nombre = forms.CharField(required=False)
    texto = forms.CharField(widget= forms.Textarea)


