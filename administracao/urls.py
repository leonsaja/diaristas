from django.urls import  path
from .views.service_views import cadastrar_servico,lista_servico,editar_servico
from .views.usuario_views import  cadastrar_usuario
app_name='administracao'
urlpatterns = [
    path('cadastrar_servico/',cadastrar_servico, name='cadastrar_servico'),
    path('',lista_servico, name='listar_servico'),
    path('editar_servico/<int:id>',editar_servico, name='editar_servico'),


   #Usuario

   path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario')
]