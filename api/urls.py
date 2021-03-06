from django.urls import  path

from api.views import diarista_localidades_view,endereco_cep_view,\
        disponibilidade_atendimento_cidade,service_view,inicio_view,usuario_view,me_view,diaria_view,pagamento_diaria_view

app_name='api'
urlpatterns = [
        path('diaristas/localidades',diarista_localidades_view.DiaristasLocalidades.as_view(), name='diaristas-localidades-lisst'),
        path('enderecos', endereco_cep_view.EnderecoCep.as_view(), name='endereco-cep-list'),
        path('diaristas/disponibilidade', disponibilidade_atendimento_cidade.DisponibilidadeAtendimento.as_view(),name='diaristas-disponibilidade-atendimento-cidade-list'),
        path('servicos', service_view.Servico.as_view(), name='servico-list'),
        path('',inicio_view.Inicio.as_view(),name='inicio'),
        path('usuario',usuario_view.Usuario.as_view(),name='usuario-list'),
        path('me', me_view.Me.as_view(), name='me-list'),
        path('diarias', diaria_view.Diaria.as_view(), name='diaria-list'),
        path('diarias/<int:diaria_id>/pagamentos',pagamento_diaria_view.PagamentoDiaria.as_view(),name='pagamento-list')
       
]
