from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import viewsets, permissions


class Medico(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    apellido = models.CharField(max_length=20, null=True)
    def __str__(self):
        return f' {self.nombre} {self.apellido}'

class Especialidad(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    dia_semana = models.CharField(max_length=20, null=True)
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.dia_semana}  {self.hora_inicio}'
# Create your models here.
class Expediente(models.Model):
    sangre = [
        ("0+","O positivo"),
        ("0-", "O negativ"),
        ("A+", "A positivo"),
        ("A-","A negativo" ),
        ("B+", "B positivo"),
        ("B-", "B negativo"),
    ]
    tipo_sangre =models.CharField(max_length=2, choices=sangre, null=True)
    alergias = models.CharField(max_length=50, null=True)
    enfermedade_heriditarias = models.CharField(max_length=50, null=True)
    tabaco = models.CharField(max_length=20, null=True)
    alcohol = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f' {self.tipo_sangre} '

class Paciente(models.Model):
    SEXO = [
        ("M", "MASCULINO"),
        ("F", "FEMENINO"),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=3)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido}'



