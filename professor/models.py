from django.db import models

# Create your models here.
from django.db.models import CharField


class Professor(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='nome'
    )
    idade = models.IntegerField(
        verbose_name='idade'
    )


    def __str__(self):
        return self.nome
