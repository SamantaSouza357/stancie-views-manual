from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from landing.models import Aluno
from landing.serializers import AlunoSerializer


# Create your views here.


class AlunoViewset(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer
