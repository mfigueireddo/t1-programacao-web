from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import SignUpForm, PerfilForm
from .models import Perfil


def signup_view(request):

    # Se o usuário já estiver logado
    if request.user.is_authenticated:
        return redirect('kanban:home')

    # Caso o usuário queira efetivar seu cadastro
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            is_mantenedor = form.cleaned_data.get('account_type', 'user') == 'mantenedor'

            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.mantenedor = is_mantenedor
            perfil.mantenedor_definido = True
            perfil.save()

            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('kanban:home')

        # else: carrega o formulário novamente

    # Caso o usuário queira preencher seu cadastro
    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html', {'form': form})


@login_required
def perfil_view(request):
    perfil_form = PerfilForm(instance=request.user)
    senha_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'salvar_perfil' in request.POST:
            perfil_form = PerfilForm(request.POST, instance=request.user)
            senha_form = PasswordChangeForm(request.user)

            if perfil_form.is_valid():
                perfil_form.save()
                messages.success(request, 'Dados do perfil atualizados com sucesso.')
                return redirect('authentication:perfil')

        elif 'salvar_senha' in request.POST:
            perfil_form = PerfilForm(instance=request.user)
            senha_form = PasswordChangeForm(request.user, request.POST)

            if senha_form.is_valid():
                user = senha_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Senha alterada com sucesso.')
                return redirect('authentication:perfil')

    return render(
        request,
        'authentication/perfil.html',
        {
            'perfil_form': perfil_form,
            'senha_form': senha_form,
        }
    )