from rest_framework import serializers
from professor.models import Professor


# fields =(__all__) para pegar todos os atributos da model no django-rest
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id','nome', 'idade')