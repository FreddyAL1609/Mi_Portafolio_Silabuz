from django import forms
from .models import portafolio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class portafolioforms(forms.ModelForm):
    class Meta:
    
        model = portafolio
        fields = ['autor', 'foto', 'titulo', 'descripcion', 'etiqueta', 'url']
        
        widgets = {
            'autor': forms.TextInput(
                attrs = {

                    'id': 'autor',
                    'type': 'hidden',
                }
            ),
        }
        
class registrofroms(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
