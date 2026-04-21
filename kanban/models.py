from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

# Obtém o modelo de usuário ativo no projeto
User = get_user_model()

class Tarefa(models.Model):
	'''
	Representa uma tarefa do Kanban.
	
    Campos:
        - Nome
        - Status (A_FAZER, EM_PROGESSO, PRONTO, ENTREGUE)
        - Descrição
        - Responsáveis
        - Story points
        - Data de criação
        - Data limite
        - Data de fechamento
        - Criador
	'''
	class Status(models.TextChoices):
		'''
		Relaciona opções de Status à diferentes strings equivalentes
		'''
		A_FAZER = 'A_FAZER', 'A Fazer'
		EM_PROGRESSO = 'EM_PROGRESSO', 'Em Progresso'
		PRONTO = 'PRONTO', 'Pronto'
		ENTREGUE = 'ENTREGUE', 'Entregue'

	nome = models.CharField(max_length=255)
	status = models.CharField(max_length=12, choices=Status.choices, default=Status.A_FAZER)
	descricao = models.TextField(blank=True)
	responsaveis = models.ManyToManyField(User, blank=True, related_name='tarefas_responsavel')
	story_points = models.PositiveSmallIntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(0), MaxValueValidator(100)],
	)
	data_criacao = models.DateTimeField(auto_now_add=True)
	data_limite = models.DateTimeField(null=True, blank=True)
	data_fechamento = models.DateTimeField(null=True, blank=True)
	# Campo utilizado para manter o nome do criador no sistema mesmo que ele delete sua conta
	criador_nome = models.CharField(max_length=150, blank=True)
	criador = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		related_name='tarefas_criadas',
		null=True,
		blank=True,
	)

	class Meta:
		'''
		Filtra as tarefas por data de criação
		'''
		ordering = ['-data_criacao']

	def __str__(self):
		'''
		Representação da tarefa em forma de string
		'''
		return self.nome

	def save(self, *args, **kwargs):
		'''
		Sobrescreve o comportamento padrão de salvamento de dados do modelo
		'''
		# Obtém o nome do criador da tarefa
		if not self.criador_nome and self.criador is not None:
			self.criador_nome = self.criador.username

        # Obtém o status anterior
		previous_status = None
		if self.pk:
			previous_status = (
				Tarefa.objects.filter(pk=self.pk).values_list('status', flat=True).first()
			)

        # Caso a tarefa esteja sendo fechada
		if self.status == self.Status.ENTREGUE and previous_status != self.Status.ENTREGUE:
			self.data_fechamento = timezone.now()
			
        # Caso a tarefa esteja sendo reaberta
		elif self.status != self.Status.ENTREGUE:
			self.data_fechamento = None

        # Aciona o salvamento real no banco de dados
		super().save(*args, **kwargs)