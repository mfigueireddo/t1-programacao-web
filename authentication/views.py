from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('kanban:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('kanban:home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication/signup.html', {'form': form})