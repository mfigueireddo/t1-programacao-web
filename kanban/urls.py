from django.urls import path

from .views import exibe_tarefas, criar_tarefa, editar_tarefa, deletar_tarefa

app_name : str = "kanban"

urlpatterns = [
    path('', exibe_tarefas, name='home'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
    path('<int:tarefa_id>/editar/', editar_tarefa, name='editar_tarefa'),
    path('<int:tarefa_id>/deletar/', deletar_tarefa, name='deletar_tarefa'),
]