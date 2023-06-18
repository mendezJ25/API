from django.forms import ModelForm, EmailInput

from pacientes.models import Paciente


class PacienteFormulario(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'edad', 'sexo', 'email', 'especialidad')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }