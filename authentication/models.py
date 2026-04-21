from django.conf import settings
from django.db import models

class Perfil(models.Model):
	'''
	Modelo de perfil do usário. Aproveita o perfil de usuário do Django.

	Possui
	- Nome de usuário
	- Email
	- Senha
	- É ou não mantenedor?
	'''
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='perfil',
	)
	mantenedor = models.BooleanField(default=False)

	def __str__(self):
		'''
		Representação do perfil em forma de string.
		'''
		tipo = 'Mantenedor' if self.mantenedor else 'Usuario'
		return f'{self.user.username} ({tipo})'
