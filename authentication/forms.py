from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Perfil

class SignUpForm(UserCreationForm):
    '''
    Gerencia o cadastro do usuário
    '''
    email = forms.EmailField(required=True, label='E-mail')

    account_type = forms.ChoiceField(
        label='Tipo de conta',
        choices=(
            # Valor interno, rótulo visível
            ('user', 'Usuário'),
            ('mantenedor', 'Mantenedor'),
        ),
        widget=forms.RadioSelect
    )

    class Meta:
        '''
        Relaciona a classe ao modelo associado e descreve quais campos entram no formulário.
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'account_type']

class PerfilForm(forms.ModelForm):
    '''
    Gerencia a exibição e edição do perfil do usuário
    '''
    email = forms.EmailField(required=True, label='E-mail')
    account_type = forms.ChoiceField(
        label='Tipo de conta',
        choices=(
            ('user', 'Usuário'),
            ('mantenedor', 'Mantenedor'),
        ),
        widget=forms.RadioSelect
    )

    class Meta:
        '''
        Relaciona a classe ao modelo associado e descreve quais campos entram no formulário.
        '''
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Assume inicialmente que a conta é do tipo usuário
        account_type = 'user'

        # Confere se a conta é tipo mantenedor
        perfil = getattr(self.instance, 'perfil', None)
        if perfil is not None and perfil.mantenedor:
            account_type = 'mantenedor'

        self.fields['account_type'].initial = account_type

    def save(self, commit=True):
        # Salva as opções de user padrão do Django
        user = super().save(commit=commit)

        # Garante que exista um perfil para o usuário
        perfil, _ = Perfil.objects.get_or_create(user=user)

        # Atualiza as permissões do usuário
        is_mantenedor = self.cleaned_data.get('account_type', 'user') == 'mantenedor'
        perfil.mantenedor = is_mantenedor
        perfil.save(update_fields=['mantenedor'])

        return user