from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from landing.models import Aluno
from landing.serializers import AlunoSerializer


# Create your views here.


class AlunoViewset(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome','^idade','=email']
    queryset = Aluno.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer
