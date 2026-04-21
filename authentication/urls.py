from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from .views import signup_view
from . import views

app_name : str = "authentication"

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='authentication:signup', permanent=False), name="home"),
    
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
]