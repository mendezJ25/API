from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from pacientes.forms import PacienteFormulario
from pacientes.models import Paciente

# Create your views here.


def agregar_paciente(request):
    pagina = loader.get_template('agregar_pacientes.html')
    if request.method == 'GET':
         formulario = PacienteFormulario
    elif request.method == 'POST':
        formulario = PacienteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_paciente(request, idPaciente):
    pagina = loader.get_template('ver_paciente.html')
    # persona = Persona.objects.get(pk=idPersona)
    paciente = get_object_or_404(Paciente, pk=idPaciente)
    mensaje = {'paciente': paciente}
    return HttpResponse(pagina.render(mensaje, request))


def editar_paciente(request, idPaciente):
    pagina = loader.get_template('editar_paciente.html')
    paciente = get_object_or_404(Paciente, pk=idPaciente)
    if request.method == "GET":
        formulario = PacienteFormulario(instance=paciente)

    elif request.method == "POST":
        formulario = PacienteFormulario(request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

    mensaje = {'formulario': formulario}

    return HttpResponse(pagina.render(mensaje, request))

def eliminar_paciente(request, idPaciente):
    paciente = get_object_or_404(Paciente, pk=idPaciente)
    if paciente:
        paciente.delete()
        return redirect('inicio')