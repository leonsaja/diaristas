from django.urls import  path

from .views import ediarista_localidades_view,endereco_cep_view,disponbilidade_atendimento_cidade,service_view
app_name='api'
urlpatterns = [
        path('diaristas/localidades',ediarista_localidades_view.DiaristasLocalidades.as_view(), name='ediaristas-localidades-lisst'),
        path('enderecos', endereco_cep_view.EnderecoCep.as_view(), name='endereco-cep-list'),
        path('diaristas/disponibilidade', disponbilidade_atendimento_cidade.DisponibilidadeAtendimento.as_view(), name='ediaristas-disponibilidade'),
        path('servicos', service_view.Servico.as_view(), name='servico-list')
]