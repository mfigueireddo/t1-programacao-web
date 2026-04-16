from django.shortcuts import render
from django.http import HttpResponse

def portal(request) -> HttpResponse:
    return render(request, "portal/portal.html")