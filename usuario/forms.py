from .models import User
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


User = get_user_model()


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=12, required=True,
                                 validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                            message='El nombre solo debe contener letras',
                                                            code='invalid_first_name')])
    last_name = forms.CharField(max_length=12, required=True,
                                validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                           message='El apellido solo debe contener letras',
                                                           code='invalid_last_name')])
    username = forms.CharField(max_length=12, required=True,
                               validators=[RegexValidator(regex='^[a-zA-Z0-9]*$',
                                                          message='El nombre de usuario debe ser alfanumerico',
                                                          code='invalid_username')])
    cedula = forms.CharField(max_length=12, required=True,
                             validators=[RegexValidator(regex='^[0-9]*$',
                                                        message='La cedula debe contener solo numeros',
                                                        code='invalid_cedula')])
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=12, required=True, widget=forms.PasswordInput)
    codigoEmpleado = forms.CharField(max_length=15, required=True,
                                     validators=[RegexValidator(regex='^[a-zA-Z0-9]*$',
                                                                message='El codigo de empleado debe ser alfa numerico',
                                                                code='invalid_codigoEmpleado')])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'cedula', 'email', 'cargo', 'password', 'codigoEmpleado')


class ActualizarUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=12, required=True,
                                 validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                            message='El nombre solo debe contener letras',
                                                            code='invalid_first_name')])
    last_name = forms.CharField(max_length=12, required=True,
                                validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                           message='El apellido solo debe contener letras',
                                                           code='invalid_last_name')])
    username = forms.CharField(max_length=12, required=True,
                               validators=[RegexValidator(regex='^[a-zA-Z0-9]*$',
                                                          message='El nombre de usuario debe ser alfanumerico',
                                                          code='invalid_username')])
    cedula = forms.CharField(max_length=12, required=True,
                             validators=[RegexValidator(regex='^[0-9]*$',
                                                        message='La cedula debe contener solo numeros',
                                                        code='invalid_cedula')])
    email = forms.EmailField(required=True)

   

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'cedula', 'email')


