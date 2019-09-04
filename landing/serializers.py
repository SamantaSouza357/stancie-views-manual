from rest_framework import serializers
from landing.models import Aluno


# fields =(__all__) para pegar todos os atributos da model no django-rest
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id','nome', 'idade', 'email')