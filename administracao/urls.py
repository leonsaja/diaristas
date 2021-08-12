from django.urls import  path
from .views.service_views import cadastrar_servico,listar_servicos,editar_servico
from .views.usuario_views import cadastrar_usuario,listar_usuarios,editar_usuario,login_usuario,deslogar_usuario
from django.contrib.auth import views as auth_views

app_name='administracao'



urlpatterns = [
    #servico
    path('servico/cadastrar/',cadastrar_servico, name='cadastrar_servico'),
    path('',listar_servicos, name='listar_servicos'),
    path('servico/editar/<int:id>',editar_servico, name='editar_servico'),

   #Usuario
   path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
   path('lista_usuarios/', listar_usuarios, name='listar_usuarios'),
   path('editar_usuario/<int:id>', editar_usuario, name='editar_usuario'),

    #autenticacao
   path('autenticacao/login/',login_usuario, name='login_usuario'),
   path('autenticacao/logout/',deslogar_usuario, name='deslogar_usuario'),

    #alteracoes de senha
   path('alterar_semha/', auth_views.PasswordChangeView.as_view(), name='logout_usuario'),

]
