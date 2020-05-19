from django.db import models

# Create your models here.

class Regiones(models.Model):
    region = models.CharField(max_length=50, blank=True, null=True)
    abreviatura = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=50, blank=True, null=True)



class Provincias(models.Model):
    provincia = models.CharField(max_length=50, blank=True, null=True)
    region = models.ForeignKey(
        'Regiones',
        on_delete=models.CASCADE,
    )


class Comunas(models.Model):
    comuna = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.ForeignKey(
        'Provincias',
        on_delete=models.CASCADE,
    )




class Calles(models.Model):
    nombre_calle = models.CharField(max_length=50, blank=True, null=True)
    comuna = models.ForeignKey(
        'Comunas',
        on_delete=models.CASCADE,
    )
