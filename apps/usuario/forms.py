import django.contrib.auth.models import User
import django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields [
            'firstname',
            'lastname',
            'email'

        ]
