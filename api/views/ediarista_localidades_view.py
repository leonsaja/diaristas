from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers.diaristas_localidade_serializer import  DiaristasLocalidadeSerializer
from ..service.cidades_atendimento_service import listar_diaristas_cidade
from ..paginations.diaristas_localidade_pagination import DiaristasLocalidadePagination
class DiaristasLocalidades(APIView,DiaristasLocalidadePagination):

    def get(self,request,format=None):
        cep = self.request.query_params.get('cep', None)
        diaristas=listar_diaristas_cidade(cep)
        resultado = self.paginate_queryset(diaristas,request)
        serializer_diaristas_localidade=DiaristasLocalidadeSerializer(resultado, many=True,context={"request":request})

        return self.get_paginated_response(serializer_diaristas_localidade.data)
