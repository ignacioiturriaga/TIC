from registration.forms import RegistrationFormUniqueEmail
from django.core.validators import RegexValidator
from django import forms
from .models import Profile

TIPO_USUARIO = (
    ('ESTUDIANTE', 'Estudiante'),
    ('COLABORADOR', 'Colaborador'),
)

class ProfileForm(RegistrationFormUniqueEmail):
    tipo_usuario = forms.CharField(label="¿Eres un colaborador de proyectos o un estudiante?",widget=forms.Select(choices=TIPO_USUARIO))
    fist_name = forms.CharField(label="Nombre Completo")
    apellido1 = forms.CharField(label="Apelldo Paterno")
    apellido2 = forms.CharField(label="Apellido Materno")
    rut = forms.CharField(label="RUT")
    telefono = forms.CharField(label="Telefono Celular +569")
    colegio = forms.CharField(label="Colegio")
    curso = forms.IntegerField(label="Curso: primero medio es 9, segundo medio es 10, etc")
    foto = forms.ImageField(label="Foto perfil")
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="El numero ingresado no es del formato: '+999999999' o no esta entre 9 y 15 digitos.")
    #phone = forms.CharField(validators=[phone_regex], label='Telefono')