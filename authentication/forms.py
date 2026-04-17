from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    '''
    Reaproveita UserCreationForm mas adiciona o opção do usuário escolher se ele será usuário ou administrador
    '''
    account_type = forms.ChoiceField(
        choices=(
            ('user', 'Usuário'),
            ('admin', 'Administrador'),
        ),
        widget=forms.RadioSelect,
        initial='user',
        label='Tipo de conta',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')