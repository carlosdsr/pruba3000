from .models import CentralesElectricas, AsociacionNodos
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


User = get_user_model()


class CentralesElectricasForm(forms.ModelForm):
    CENTRALES_CHOICES = (
        ('Centrales de Generacion', 'Centrales de Generacion'),
        ('Centrales Termoelectricas', 'Centrales Termoelectricas'),
        ('Centros de Distribucion', 'Centros de Distribucion'),
    )

    nombre = forms.CharField(max_length=50, required=True,
                             validators=[RegexValidator(regex='^[a-zA-Z]*$',
                                                        message='El nombre solo debe contener letras',
                                                        code='invalid_nombre')])
    ubicacionGeografica = forms.CharField(max_length=50, required=True)
    tipoDeNodo = forms.ChoiceField(choices=CENTRALES_CHOICES, required=True)

    class Meta:
        model = CentralesElectricas
        fields = ('nombre', 'ubicacionGeografica', 'tipoDeNodo')


class ImprimirCentral1Form(forms.Form):
    central1 = forms.ModelChoiceField(queryset=CentralesElectricas.objects.all())


class ImprimirCentral2Form(forms.Form):
    central2 = forms.ModelChoiceField(queryset=CentralesElectricas.objects.all())


class ImprimirCentral3Form(forms.Form):
    central3 = forms.ModelChoiceField(queryset=CentralesElectricas.objects.all(), required=False)

class ImprimirKWsForm(forms.Form):
    NombreAsociacion= forms.ModelChoiceField(queryset=AsociacionNodos.objects.all(), required=False)







class asociacionNodosForm(forms.ModelForm):
    ASOCIACION_CHOICES = (
        ('C.Generacion->C.Termoelectricas->C.Distribucion', 'C.Generacion->C.Termoelectricas->C.Distribucion'),
        ('C.Generacion->C.Distribucion', 'C.Generacion->C.Distribucion'),
        ('C.Termoelectricas->C.Distribucion', 'C.Termoelectricas->C.Distribucion'),
        ('C.Distribucion->C.Distribucion', 'C.Distribucion->C.Distribucion'),
    )
    nombreAsociacion = forms.CharField(max_length=50, required=True)
    nodo1 = forms.CharField(max_length=50, required=True)
    nodo2 = forms.CharField(max_length=50, required=True)
    nodo3 = forms.CharField(max_length=50, required=False)
    KWs = forms.CharField(max_length=50, required=True,
                             validators=[RegexValidator(regex='^[0-9]*$',
                                                        message='Los KWs solo debe contener numeros',
                                                        code='invalid_nombre')])
    tipoAsociacion = forms.ChoiceField(choices=ASOCIACION_CHOICES, required=True)

    class Meta:
        model = AsociacionNodos
        fields = ('nodo1', 'nodo2', 'nodo3', 'KWs', 'tipoAsociacion', 'nombreAsociacion')

class editarNodosForm(forms.ModelForm):

    nombreAsociacion = forms.CharField(max_length=50, required=True)
    KWs = forms.CharField(max_length=50, required=True,
                             validators=[RegexValidator(regex='^[0-9]*$',
                                                        message='Los KWs solo debe contener numeros',
                                                        code='invalid_nombre')])
    

    class Meta:
        model = AsociacionNodos
        fields = ( 'KWs','nombreAsociacion')
