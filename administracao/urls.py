from django.urls import  path
from .views.service_views import cadastrar_servico,listar_servicos,editar_servico
from .views.usuario_views import cadastrar_usuario,listar_usuarios
app_name='administracao'
urlpatterns = [
    path('cadastrar_servico/',cadastrar_servico, name='cadastrar_servico'),
    path('',listar_servicos, name='listar_servico'),
    path('editar_servico/<int:id>',editar_servico, name='editar_servico'),


   #Usuario

   path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
   path('lista_usuarios/', listar_usuarios, name='listar_usuarios')

]