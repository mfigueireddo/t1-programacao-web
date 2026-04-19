from django.conf import settings
from django.db import models

class Perfil(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='perfil',
	)
	mantenedor = models.BooleanField(default=False)
	mantenedor_definido = models.BooleanField(default=False)

	def __str__(self):
		'''
		Representação da tarefa em forma de string
		'''
		tipo = 'Mantenedor' if self.mantenedor else 'Usuario'
		return f'{self.user.username} ({tipo})'

	def save(self, *args, **kwargs):
		'''
		Sobrescreve o comportamento padrão de salvamento de dados do modelo
		'''
		# Define o papel uma única vez. Depois disso, fica imutável
		if self.pk:
			perfil_atual = Perfil.objects.filter(pk=self.pk).values(
				'mantenedor',
				'mantenedor_definido',
			).first()
			
			if perfil_atual is not None:
				if perfil_atual['mantenedor_definido']:
					self.mantenedor = perfil_atual['mantenedor']
					self.mantenedor_definido = True

		super().save(*args, **kwargs)
