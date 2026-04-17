from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    '''
    Reaproveita UserCreationForm e adiciona a opcao de escolher
    se a conta sera de usuario comum ou mantenedor.
    '''
    account_type = forms.ChoiceField(
        choices=(
            ('user', 'Usuário'),
            ('mantenedor', 'Mantenedor'),
        ),
        widget=forms.RadioSelect,
        initial='user',
        label='Tipo de conta',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')