from django.shortcuts import render
from landing.models import Aluno

# Create your views here.

from rest_framework import viewsets

from landing.serializers import AlunoSerializer


class AlunoViewset(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
