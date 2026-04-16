from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('portal:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('portal:home')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/signup.html', {'form': form})