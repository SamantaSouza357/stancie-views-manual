from rest_framework import serializers

from landing.serializers import AlunoSerializer
from professor.models import Professor


# fields =(__all__) para pegar todos os atributos da model no django-rest
class ProfessorSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        nome = serializers.CharField(max_length=255, required=True)
        idade = serializers.IntegerField()
        alunos = AlunoSerializer(many=True, read_only=True)

        def create (self, validated_data):
             professor = Professor.objects.create(**validated_data)
             return professor
        def update(self, instance, validated_data):
            instance.nome = validated_data.get('nome')
            instance.idade = validated_data.get('idade')
            instance.save()
            return instance
