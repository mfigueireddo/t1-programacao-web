from django import forms

from .models import Tarefa

class TarefaCreateForm(forms.ModelForm):
    '''
    Formulário de criação da tarefa
    '''
    class Meta:
        model = Tarefa
        fields = [
            'nome',
            'status',
            'descricao',
            'story_points',
            'data_limite',
            'responsaveis',
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'kanban-criar-form-input',
                    'placeholder': 'Digite o titulo da tarefa',
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'kanban-criar-form-input'
                }
            ),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'kanban-criar-form-input',
                    'rows': 5,
                    'placeholder': 'Digite os detalhes da tarefa',
                }
            ),

            'story_points': forms.NumberInput(
                attrs={
                    'class': 'kanban-criar-form-input',
                    'min': 0,
                    'max': 100,
                    'placeholder': '0',
                }
            ),

            'data_limite': forms.DateTimeInput(
                attrs={'class': 'kanban-criar-form-input', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),

            'responsaveis': forms.CheckboxSelectMultiple(),
        } # widgets

        labels = {
            'nome': 'Nome da Tarefa',
            'descricao': 'Descrição',
            'story_points': 'Story Points (0-100)',
            'data_limite': 'Data Limite',
            'responsaveis': 'Responsáveis',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].choices = [('', 'Selecione um status')] + list(
            Tarefa.Status.choices
        )

        self.fields['data_limite'].input_formats = ['%Y-%m-%dT%H:%M']

class TarefaMantenedorUpdateForm(forms.ModelForm):
    '''
    Formulario de edicao de tarefa (pelo mantenedor)
    '''
    class Meta:
        model = Tarefa
        fields = [
            'nome',
            'status',
            'descricao',
            'story_points',
            'data_limite',
            'responsaveis',
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'kanban-editar-form-input'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'kanban-editar-form-input'
                }
            ),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'kanban-editar-form-input', 'rows': 5
                }
            ),

            'story_points': forms.NumberInput(
                attrs={'class': 'kanban-editar-form-input', 'min': 0, 'max': 100}
            ),

            'data_limite': forms.DateTimeInput(
                attrs={'class': 'kanban-editar-form-input', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),

            'responsaveis': forms.CheckboxSelectMultiple(),
        } # widgets

        labels = {
            'nome': 'Nome da Tarefa',
            'descricao': 'Descrição',
            'story_points': 'Story Points (0-100)',
            'data_limite': 'Data Limite',
            'responsaveis': 'Responsáveis',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_limite'].input_formats = ['%Y-%m-%dT%H:%M']

        data_limite = self.instance.data_limite
        if data_limite:
            self.initial['data_limite'] = data_limite.strftime('%Y-%m-%dT%H:%M')

class TarefaUsuarioComumUpdateForm(forms.Form):
    '''
    Formulário de edição de tarefa (pelo usuário comum)
    '''
    ACAO_ADICIONAR = 'adicionar'
    ACAO_REMOVER = 'remover'
    ACAO_MANTER = 'manter'

    status = forms.ChoiceField(
        choices=Tarefa.Status.choices, 
        required=True
    )

    data_criacao = forms.CharField(
        required=False,
        disabled=True,
        label='Data de Criação',
    )

    data_fechamento = forms.CharField(
        required=False,
        disabled=True,
        label='Data de Fechamento',
    )

    acao_responsavel = forms.ChoiceField(
        label='Ação do responsável',
        widget=forms.RadioSelect, 
        required=True
    )

    def __init__(self, *args, **kwargs):
        self.tarefa = kwargs.pop('tarefa')
        self.user = kwargs.pop('user')
        self.can_edit_status = kwargs.pop('can_edit_status', False)
        super().__init__(*args, **kwargs)

        self.fields['status'].label = 'Mudar Status'
        self.fields['status'].widget.attrs.update({'class': 'kanban-editar-form-input'})
        self.fields['data_criacao'].widget.attrs.update({'class': 'kanban-editar-form-input'})
        self.fields['data_fechamento'].widget.attrs.update({'class': 'kanban-editar-form-input'})

        self.fields['data_criacao'].initial = self.tarefa.data_criacao.strftime('%d/%m/%Y %H:%M')
        if self.tarefa.data_fechamento:
            self.fields['data_fechamento'].initial = self.tarefa.data_fechamento.strftime('%d/%m/%Y %H:%M')
        else:
            self.fields['data_fechamento'].initial = 'Nao fechada'

        # Se o usuário for responsável pela tarefa
        if self.user in self.tarefa.responsaveis.all():
            self.fields['acao_responsavel'].choices = [
                (self.ACAO_REMOVER, 'Remover minha responsabilidade'),
                (self.ACAO_MANTER, 'Manter minha responsabilidade'),
            ]
            self.fields['acao_responsavel'].initial = self.ACAO_MANTER

        # Se o usuário NÃO for responsável pela tarefa
        else:
            self.fields['acao_responsavel'].choices = [
                (self.ACAO_ADICIONAR, 'Adicionar minha responsabilidade'),
                (self.ACAO_MANTER, 'Manter sem responsabilidade'),
            ]
            self.fields['acao_responsavel'].initial = self.ACAO_MANTER

        self.fields['status'].initial = self.tarefa.status

        # Usuário comum só pode alterar o status se for responsável pela tarefa.
        if not self.can_edit_status:
            self.fields['status'].disabled = True
            self.fields['status'].required = False

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if not self.can_edit_status:
            return self.tarefa.status
        return status

    def save(self):
        if self.can_edit_status:
            self.tarefa.status = self.cleaned_data['status']

        acao_responsavel = self.cleaned_data['acao_responsavel']
        if acao_responsavel == self.ACAO_ADICIONAR:
            self.tarefa.responsaveis.add(self.user)
        elif acao_responsavel == self.ACAO_REMOVER:
            self.tarefa.responsaveis.remove(self.user)

        self.tarefa.save()
        return self.tarefa

class DeleteTarefaForm(forms.Form):
    '''
    Formulário de deleção de tarefa
    '''
    confirm = forms.BooleanField(
        required=True,
        label='Sim, tenho certeza que desejo deletar esta tarefa',
        error_messages={'required': 'Confirme a exclusao para deletar a tarefa.'},
    )
