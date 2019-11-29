from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=13, verbose_name='CPF')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
