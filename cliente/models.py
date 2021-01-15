from django.db import models

class Cliente(models.Model):
	name = models.CharField("Nome", max_length=50)
	address = models.CharField("Endereço", max_length=100)
	phone = models.CharField("Telefone", max_length=11)
	birthday = models.DateField("Data de Nascimento")
	date_register = models.DateTimeField("Data do Registro", auto_now_add=True)

	def __str__(self):
		return self.name


