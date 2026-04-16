from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def kanban_view(request):
    return render(request, 'kanban/kanban.html')