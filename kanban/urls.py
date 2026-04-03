from django.urls import path
from .views import signup_view, kanban_view

urlpatterns = [
    path('', kanban_view, name='kanban'),
    path('signup/', signup_view, name='signup'),
]