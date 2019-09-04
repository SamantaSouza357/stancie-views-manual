from django.shortcuts import render
from professor.models import Professor

# Create your views here.

from rest_framework import viewsets

from professor.serializers import ProfessorSerializer


class ProfessorViewset(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

# Create your views here.
