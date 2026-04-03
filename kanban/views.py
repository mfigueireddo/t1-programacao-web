from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('kanban')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('kanban')
    else:
        form = UserCreationForm()

    return render(request, 'kanban/signup.html', {'form': form})


@login_required
def kanban_view(request):
    return render(request, 'kanban/kanban.html')