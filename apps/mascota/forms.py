from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'folio',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacunas'
        ]

        labels = {
            'folio' : 'Folio',
            'nombre' : 'Nombre',
            'sexo' : 'Sexo',
            'edad_aproximada' : 'Edad aproximada',
            'fecha_rescate' : 'Fecha de rescate',
            'persona' : 'Adoptante',
            'vacunas' : 'Vacunas'
        }

        widgets = {
            'folio' : forms.TextInput(attrs={'class' : 'form-control'}),
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'sexo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'edad_aproximada' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha_rescate' : forms.DateInput(attrs={'class' : 'form-control'}),
            'persona' : forms.Select(attrs={'class' : 'form-control'}   ),
            'vacunas' : forms.CheckboxSelectMultiple()
        }
