from django.contrib import admin

from pacientes.models import Paciente, Especialidad, Medico, Expediente

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Expediente)