from rest_framework import  serializers
from administracao.models import  Service

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields= '__all__'

