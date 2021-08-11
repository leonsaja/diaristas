from django.urls import  path
from .views import cadastrar_servico,lista_servico,editar_servico
app_name='administracao'
urlpatterns = [
    path('cadastrar_servico/',cadastrar_servico, name='cadastrar_servico'),
    path('lista_servico/',lista_servico, name='listar_servico'),
    path('editar_servico/<int:id>',editar_servico, name='editar_servico'),
   
]