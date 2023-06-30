from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from pacientes.models import Paciente


# Create your views here.
def mostrar_pacientes(request):
     cantidad_pacientes = Paciente.objects.count()
     pagina = loader.get_template('pacientes.html')
     # nombres_pacientes = Paciente.objects.all()
     nombres_pacientes = Paciente.objects.order_by('apellido')

     datos = {'cantidad': cantidad_pacientes, 'pacientes':nombres_pacientes}


     return HttpResponse(pagina.render(datos, request))


