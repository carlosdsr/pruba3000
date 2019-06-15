from django.db import models


class CentralesElectricas(models.Model):
    CENTRALES_CHOICES = (
        ('Centrales de Generacion', 'Centrales de Generacion'),
        ('Centrales Termoelectricas', 'Centrales Termoelectricas'),
        ('Centros de Distribucion', 'Centros de Distribucion'),
    )
    nombre = models.CharField(max_length=50)
    ubicacionGeografica = models.CharField(max_length=50)
    tipoDeNodo = models.CharField(max_length=100, choices=CENTRALES_CHOICES)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.tipoDeNodo)

class AsociacionNodos(models.Model):
    ASOCIACION_CHOICES = (
        ('C.Generacion->C.Termoelectricas->C.Distribucion', 'C.Generacion->C.Termoelectricas->C.Distribucion'),
        ('C.Generacion->C.Distribucion', 'C.Generacion->C.Distribucion'),
        ('C.Termoelectricas->C.Distribucion', 'C.Termoelectricas->C.Distribucion'),
        ('C.Distribucion->C.Distribucion', 'C.Distribucion->C.Distribucion'),
    )
    nombreAsociacion = models.CharField(max_length=50)
    nodo1 = models.CharField(max_length=50)
    nodo2 = models.CharField(max_length=50)
    nodo3 = models.CharField(max_length=50)
    KWs = models.CharField(max_length=50)
    tipoAsociacion = models.CharField(max_length=100, choices=ASOCIACION_CHOICES)
    def __str__(self):
        return (self.nombreAsociacion)

