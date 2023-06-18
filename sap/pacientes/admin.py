from django.contrib import admin

from pacientes.models import Paciente, Especialidad, Medico

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Especialidad)
admin.site.register(Medico)