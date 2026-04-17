from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup_view(request):

    # Se o usuário já estiver logado
    if request.user.is_authenticated:
        return redirect('kanban:home')

    # Caso o usuário queira efetivar seu cadastro
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            is_admin = form.cleaned_data['account_type'] == 'admin'

            user.is_staff = is_admin
            user.is_superuser = is_admin
            user.save()

            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('kanban:home')
        
    # Caso o usuário queira preencher seu cadastro
    form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})