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
            ('user', 'Usuário'),
            ('mantenedor', 'Mantenedor'),
        ),
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'account_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


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
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        account_type = 'user'
        perfil = getattr(self.instance, 'perfil', None)
        if perfil is not None and perfil.mantenedor:
            account_type = 'mantenedor'

        self.fields['account_type'].initial = account_type

    def save(self, commit=True):
        user = super().save(commit=commit)

        perfil, _ = Perfil.objects.get_or_create(user=user)
        is_mantenedor = self.cleaned_data.get('account_type', 'user') == 'mantenedor'

        # Usa update para não acionar a regra de imutabilidade do método save do Perfil.
        Perfil.objects.filter(pk=perfil.pk).update(
            mantenedor=is_mantenedor,
            mantenedor_definido=True,
        )

        return user