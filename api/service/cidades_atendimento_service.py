import json
import requests
from rest_framework import serializers
from ..models import CidadesAtendimento


def listar_diaristas_cidade(cep):
    codigo_ibge=buscar_cidade_cep(cep)['ibge']
    try:
        cidade=CidadesAtendimento.objects.get(codigo_ibge=codigo_ibge)
        return cidade.usuario.filter(tipo_usuario=2).order_by('-reputacao')
    except:
        return []

def verificar_disponibilidade_cidade(cep):
    codigo_ibge=buscar_cidade_cep(cep)['ibge']
    return CidadesAtendimento.objects.filter(codigo_ibge=codigo_ibge).exists()

def buscar_cidade_cep(cep):
    requisicao=requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )

    if requisicao.status_code == 400:
        raise serializers.ValidationError({"Detail":"Erro ao Buscar o CEP"})
    cidade_api = json.loads(requisicao.content)

    if 'erro' in cidade_api:

        print('erro')
        raise serializers.ValidationError({"detail":"O CEP informado não foi encontrado"})
    return cidade_api