from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


#En este apartado decidi incluir un email por si la facultad desea comunicarse con el alumno

class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    



class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)



class CalificacionForm(forms.Form):
    NombreMateria = forms.CharField(max_length=50, required=True)
    NombreAlumno = forms.CharField(max_length=50,required=True)
    nota = forms.IntegerField(required=True)    


class ModeloForms(forms.Form):
    NombreMateria = forms.CharField(max_length=50, required=True)
    dia = forms.CharField(max_length=50, required=True)
    imagen = forms.ImageField(required=True)

