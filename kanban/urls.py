from django.urls import path
from .views import kanban_view

app_name : str = "kanban"

urlpatterns = [
    path('', kanban_view, name='home'),
]