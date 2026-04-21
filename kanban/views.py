from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Prefetch

from .models import Tarefa
from .forms import (
    DeleteTarefaForm,
    TarefaMantenedorUpdateForm,
    TarefaCreateForm,
    TarefaUsuarioComumUpdateForm,
)

def is_mantenedor(user):
    '''
    Confere se o usuario é mantenedor

    Necessário para gerenciamento de permissões
    '''
    # Procura o usuário e o campo mantenedor dentro do perfil e transforma o resultado em booleano
    return bool(getattr(getattr(user, 'perfil', None), 'mantenedor', False))

@login_required
def exibe_tarefas(request):
    # Pré-carrega todas aas tarefas, criadores e responsáveis
    tarefas = (
        # Carrega todas as tarefas e traz o criador junto via JOIN
        Tarefa.objects.select_related('criador')
        # Busca todos os responsáveis daquela tarefa
        .prefetch_related(Prefetch('responsaveis'))
        .all()
    )

    is_mantenedor_user = is_mantenedor(request.user)

    # Separa as tarefas pelo seu status
    status_columns = []
    for status_value, status_label in Tarefa.Status.choices:
        tarefas_coluna = []

        for tarefa in tarefas:
            # Filtra as tarefas pelo statsu
            if tarefa.status != status_value:
                continue

            # Obtém informações específicas daquela tarefa
            tarefas_coluna.append(
                {
                    'item': tarefa,
                    'can_delete': is_mantenedor_user,
                }
            )

        # Relaciona todas as tarefas daquele coluna
        status_columns.append(
            {
                'value': status_value,
                'label': status_label,
                'tarefas': tarefas_coluna,
            }
        )

    return render(
        request,
        'kanban/kanban.html',
        {
            'status_columns': status_columns,
            'is_mantenedor_user': is_mantenedor_user,
        }
    )

@login_required
def criar_tarefa(request):
    '''
    Gerencia a criação de uma tarefa

    Somente mantenedores podem realizar a acao

    Uma lista com todos os usuarios disponiveis e enviada ao mantenedor para alocacao
    '''
    
    # Validação do usuário
    if not is_mantenedor(request.user):
        messages.error(request, 'Você não tem permissão para criar tarefas.')
        return redirect('kanban:home')

    form = TarefaCreateForm(request.POST or None)

    # Usuário envia o formulário
    if request.method == 'POST' and form.is_valid():
        # O criador deve ser salvo manualmente, pois esse dado não vem do input via formulário
        tarefa = form.save(commit=False)
        tarefa.criador = request.user
        tarefa.save()
        # Cria a relação many-to-many dos usuários
        form.save_m2m()

        messages.success(request, f'Tarefa "{tarefa.nome}" criada com sucesso!')
        return redirect('kanban:home')

    return render(
        request,
        'kanban/criar_tarefa.html',
        {
            'form': form,
        }
    )

@login_required
def editar_tarefa(request, tarefa_id):
    '''
    Gerencia a edição de uma tarefa

    Usuário "comum" pode editar:
    - Status (se responsável)
    - Responsáveis (adicionar/remover a si mesmo)
    
    Mantenedor pode editar:
    - Nome
    - Status
    - Descrição
    - Responsáveis
    - Story points
    - Data limite
    '''
    # Obtém a tarefa
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    # Verifica as permissões
    is_mantenedor_user = is_mantenedor(request.user)
    is_responsavel = request.user in tarefa.responsaveis.all()
    
    # Obtém o formulário correspondente
    if is_mantenedor_user:
        form = TarefaMantenedorUpdateForm(
            request.POST or None, 
            instance=tarefa
        )
    else:
        form = TarefaUsuarioComumUpdateForm(
            request.POST or None,
            tarefa=tarefa,
            user=request.user,
            can_edit_status=is_responsavel,
        )

    # Usuário envia o formulário
    if request.method == 'POST' and form.is_valid():
        tarefa = form.save()

        messages.success(request, f'Tarefa "{tarefa.nome}" atualizada com sucesso!')
        return redirect('kanban:home')

    return render(
        request,
        'kanban/editar_tarefa.html',
        {
            'tarefa': tarefa,
            'form': form,
            'is_mantenedor_user': is_mantenedor_user,
            'is_responsavel': is_responsavel,
        }
    )

@login_required
def deletar_tarefa(request, tarefa_id):
    '''
    Gerencia a deleção de uma tarefa

    So um mantenedor pode fazer isso
    '''
    if not is_mantenedor(request.user):
        messages.error(request, 'Você não tem permissão para deletar tarefas.')
        return redirect('kanban:home')

    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    form = DeleteTarefaForm(request.POST or None)

    # Usuário envia o formulário
    if request.method == 'POST' and form.is_valid():

        nome_tarefa = tarefa.nome
        tarefa.delete()
        messages.success(request, f'Tarefa "{nome_tarefa}" deletada com sucesso!')
        return redirect('kanban:home')
    
    # Usuário quer preencher o formulário
    return render(
        request,
        'kanban/deletar_tarefa.html',
        {
            'tarefa': tarefa,
            'form': form,
        }
    )