from django import forms
from usuario.models import User


class InicioSesionForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput())


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'cedula', 'email', 'cargo', 'password', 'codigoEmpleado')
