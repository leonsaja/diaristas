from rest_framework.views import APIView
from rest_framework.response import  Response
from api.serializers.endereco_cep_serializer import EnderecoCepSerializer
from api.service.cidades_atendimento_service import buscar_cidade_cep
from rest_framework import  status

class EnderecoCep(APIView):
    def get(self,request, format=None):
        cep= self.request.query_params.get('cep',None)
        endereco=buscar_cidade_cep(cep)
        serializer_endereco_cep=EnderecoCepSerializer(endereco)
        return Response(serializer_endereco_cep.data, status=status.HTTP_200_OK)