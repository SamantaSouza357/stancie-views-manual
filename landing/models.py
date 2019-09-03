from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='nome'
    )
    idade = models.CharField(
        max_length=50,
        verbose_name='idade'
    )
    email = models.CharField(
        max_length=50,
        verbose_name='email'
    )

    def __str__(self):
        return self.nome

