from rest_framework import serializers

from pacientes.models import Medico, Especialidad, Expediente, Paciente


class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ['nombre','apellido']


class EspecialidadSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer
    class Meta:
        model = Especialidad
        fields = ['nombre','dia_semana','hora_inicio']

class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediente
        fields = ['tipo_sangre']

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    especialidad = EspecialidadSerializer()
    expediente = ExpedienteSerializer()
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'sexo', 'email', 'especialidad', 'expediente']