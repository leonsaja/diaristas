from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import  status
from administracao.service.servico_service import  listar_servicos
from ..serializers.servico_serializer import ServicoSerializer

class Servico(APIView):

    def get(self,request, format=None):
        servicos=listar_servicos()
        serializer_servico=ServicoSerializer(servicos,many=True)
        return Response(serializer_servico.data, status=status.HTTP_200_OK)