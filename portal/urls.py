from django.urls import path

from portal import views

app_name : str = "portal"

urlpatterns : list = [
    path('', views.portal, name='portal'),
]