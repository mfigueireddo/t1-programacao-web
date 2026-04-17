from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Tarefa
from django.contrib.auth import get_user_model

User = get_user_model()

def is_admin(user):
    '''
    Confere se o usuário é administrador

    Necessário para gerenciamento de permissões
    '''
    return user.is_staff or user.is_superuser

@login_required
def exibe_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'kanban/kanban.html', {
        'tarefas': tarefas,
        'status_choices': Tarefa.Status.choices,
    })

@login_required
@user_passes_test(is_admin)
def criar_tarefa(request):
    '''
    Gerencia a criação de uma tarefa

    Somente administradores podem realizar a ação

    Uma lista com todos os usuários disponíveis é enviada ao administrador para que a tarefa possa ser alocada
    '''
    
    # Usuário envia o formulário
    if request.method == 'POST':
        nome = request.POST.get('nome')
        status = request.POST.get('status')
        descricao = request.POST.get('descricao', '')
        story_points = request.POST.get('story_points')
        data_limite = request.POST.get('data_limite', None) or None
        
        responsaveis_ids = request.POST.getlist('responsaveis')
        
        # Validação dos story points
        try:
            story_points = int(story_points) if story_points else None
        except ValueError:
            messages.error(request, 'Story points deve ser um número válido.')
            return redirect('kanban:criar_tarefa')
        
        # Cria o objeto no banco de dados
        tarefa = Tarefa.objects.create(
            nome=nome,
            status=status,
            descricao=descricao,
            story_points=story_points,
            data_limite=data_limite,
            criador=request.user
        )

        # Atribui os responsáveis
        if responsaveis_ids:
            tarefa.responsaveis.set(responsaveis_ids)
        
        messages.success(request, f'Tarefa "{nome}" criada com sucesso!')
        return redirect('kanban:home')
    
    # Usuário quer preencher o formulário
    usuarios = User.objects.all()
    return render(request, 'kanban/criar_tarefa.html', {
        'usuarios': usuarios,
        'status_choices': Tarefa.Status.choices
    })


@login_required
def editar_tarefa(request, tarefa_id):
    '''
    Gerencia a edição de uma tarefa

    Usuário "comum" pode editar:
    - Status (se responsável)
    - Responsáveis (adicionar/remover a si mesmo)
    
    Administrador pode editar:
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
    is_admin_user = is_admin(request.user)
    is_responsavel = request.user in tarefa.responsaveis.all()
    
    # Validação do usuário
    if not is_admin_user and not is_responsavel:
        messages.error(request, 'Você não tem permissão para editar esta tarefa.')
        return redirect('kanban:home')
    
    # Usuário envia o formulário
    if request.method == 'POST':

        # Edição: administrador
        if is_admin_user:
            tarefa.nome = request.POST.get('nome', tarefa.nome)
            tarefa.status = request.POST.get('status', tarefa.status)
            tarefa.descricao = request.POST.get('descricao', tarefa.descricao)
            
            story_points = request.POST.get('story_points')
            # Validação do valor dos story points
            try:
                tarefa.story_points = int(story_points) if story_points else None
            except ValueError:
                messages.error(request, 'Story points deve ser um número válido.')
                return redirect('kanban:editar_tarefa', tarefa_id=tarefa.id)
            
            tarefa.data_limite = request.POST.get('data_limite', None) or None
            
            responsaveis_ids = request.POST.getlist('responsaveis')
            tarefa.responsaveis.set(responsaveis_ids)

        # Edição: usuário comum
        else:
            novo_status = request.POST.get('status')
            if novo_status and novo_status != tarefa.status:
                tarefa.status = novo_status
            
            acao_responsavel = request.POST.get('acao_responsavel')
            if acao_responsavel == 'adicionar':
                tarefa.responsaveis.add(request.user)
            elif acao_responsavel == 'remover':
                tarefa.responsaveis.remove(request.user)
            # 'manter' ou valor ausente não alteram a responsabilidade atual
        
        tarefa.save()
        messages.success(request, f'Tarefa "{tarefa.nome}" atualizada com sucesso!')
        return redirect('kanban:home')
    
    # Usuário quer preencher o formulário
    usuarios = User.objects.all()
    return render(request, 'kanban/editar_tarefa.html', {
        'tarefa': tarefa,
        'usuarios': usuarios,
        'status_choices': Tarefa.Status.choices,
        'is_admin_user': is_admin_user,
        'is_responsavel': is_responsavel
    })


@login_required
@user_passes_test(is_admin)
def deletar_tarefa(request, tarefa_id):
    '''
    Gerencia a deleção de uma tarefa

    Só um administrador pode fazer isso
    '''
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    # Usuário envia o formulário
    if request.method == 'POST':
        nome_tarefa = tarefa.nome
        tarefa.delete()
        messages.success(request, f'Tarefa "{nome_tarefa}" deletada com sucesso!')
        return redirect('kanban:home')
    
    # Usuário quer preencher o formulário
    return render(request, 'kanban/deletar_tarefa.html', {'tarefa': tarefa})