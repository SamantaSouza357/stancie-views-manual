from django.db import models

# Create your models here.
from django.db.models import CharField

from professor.models import Professor


class Aluno(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='nome'
    )
    idade = models.IntegerField(
        verbose_name='idade'
    )
    email = models.EmailField(
        max_length=50,
        verbose_name='email'
    )
    prof_favorito = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='alunos'
    )

    def __str__(self):
        return self.nome

