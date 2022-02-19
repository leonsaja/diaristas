from rest_framework.views import APIView
from ..hateoas import  Hateoas
from django.urls import  reverse
from rest_framework.response import Response
from rest_framework import status

class Inicio(APIView):

    def get(self,request,format=None):

        links=Hateoas()
        links.add_get('listar_servicos',reverse('api:servico-list'))
        links.add_get('endereco_cep', reverse('api:endereco-cep-list'))
        links.add_get('diaristas_localidade', reverse('api:diaristas-localidades-lisst'))
        links.add_get('verificar_disponibilidade_atendimento',reverse('api:diaristas-disponibilidade-atendimento-cidade-list'))
        links.add_post('cadastrar_usuario',reverse('api:usuario-list'))
        links.add_post('login',reverse('token_obtain_pair'))
        links.add_post('logout', reverse('logout-list'))
        links.add_get('usuario_logado',reverse('api:me-list'))
        return Response({"links":links.to_array()},status=status.HTTP_200_OK)
