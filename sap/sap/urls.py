"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pacientes.views import agregar_paciente, ver_paciente,editar_paciente,eliminar_paciente,generar_reporte
from webapp.views import mostrar_pacientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_pacientes, name= 'inicio'),
    path('agregar_pacientes/', agregar_paciente),
    path('ver_paciente/<int:idPaciente>', ver_paciente),
    path('editar_paciente/<int:idPaciente>', editar_paciente),
    path('eliminar_paciente/<int:idPaciente>', eliminar_paciente),
    path('generar_reporte/', generar_reporte),

]
