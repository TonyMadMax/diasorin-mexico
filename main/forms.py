from django import forms
from django.contrib.auth.models import User
from main.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {
            'username': ('Nombre de Usuario'),
            'email':('Correo Electrónico'),
            'password': ('Contraseña'),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        labels = {'profile_pic': ('Foto de perfil'),}
