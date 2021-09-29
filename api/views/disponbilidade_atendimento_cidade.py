from rest_framework.response import  Response

from api.service import cidades_atendimento_service
from api.service.cidades_atendimento_service import buscar_cidade_cep
from  rest_framework.views import  APIView



class DisponibilidadeAtendimento(APIView):

    def get(self,request, format=None):
        cep =self.request.query_params.get('cep',None)
        disponibilidade=cidades_atendimento_service.verificar_disponibilidade_cidade(cep)
        return Response({"disponibilidade":disponibilidade})
