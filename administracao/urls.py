from django.urls import path, reverse_lazy
from .views.service_views import cadastrar_servico,listar_servicos,editar_servico
from .views.usuario_views import cadastrar_usuario,listar_usuarios,editar_usuario
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cbaf1d1e81a58c4671f089b0910e966b481efa09
from django.contrib.auth import views as auth_views

=======
>>>>>>> parent of 3451a08... autenticacao  finalizada
app_name='administracao'
urlpatterns = [
<<<<<<< HEAD

    #servico
    path('servicos/cadastrar/',cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar',listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>',editar_servico, name='editar_servico'),

   #Usuario
   path('usuario/cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
   path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
   path('usuario/editar/<int:id>', editar_usuario, name='editar_usuario'),

   #autenticacao
   path('autenticacao/login', auth_views.LoginView.as_view(),name='login_usuario'),
   path('autenticacao/logout', auth_views.LogoutView.as_view(),name='deslogar_usuario'),

   path('alterar_senha', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('administracao:listar_servicos')), name='alterar_senha'),
   path('resetar_senha',auth_views.PasswordResetView.as_view(),
         name='resetar_senha'),
    path('resetar_senha/sucesso',auth_views.PasswordResetDoneView.as_view(),
         name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>',auth_views.PasswordResetConfirmView.as_view(),
         name='resetar_senha_confirmar'),
    path('resetar_senha/feito',auth_views.PasswordResetDoneView.as_view(), name='resetar_senha_feito'),

]
=======
    path('cadastrar_servico/',cadastrar_servico, name='cadastrar_servico'),
    path('',listar_servicos, name='listar_servico'),
    path('editar_servico/<int:id>',editar_servico, name='editar_servico'),

<<<<<<< HEAD

   #Usuario

   path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
   path('lista_usuarios/', listar_usuarios, name='listar_usuarios'),
   path('editar_usuario/<int:id>', editar_usuario, name='editar_usuario'),
=======
urlpatterns = [

    #servico
    path('servicos/cadastrar/',cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar',listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>',editar_servico, name='editar_servico'),

   #Usuario
   path('usuario/cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
   path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
   path('usuario/editar/<int:id>', editar_usuario, name='editar_usuario'),

   #autenticacao
   path('autenticacao/login', auth_views.LoginView.as_view(),name='login_usuario'),
   path('autenticacao/logout', auth_views.LogoutView.as_view(),name='deslogar_usuario'),

   path('alterar_senha', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('administracao:listar_servicos')), name='alterar_senha'),
   path('resetar_senha',auth_views.PasswordResetView.as_view(),
         name='resetar_senha'),
    path('resetar_senha/sucesso',auth_views.PasswordResetDoneView.as_view(),
         name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uidb64>/<str:token>',auth_views.PasswordResetConfirmView.as_view(),
         name='resetar_senha_confirmar'),
    path('resetar_senha/feito',auth_views.PasswordResetDoneView.as_view(), name='resetar_senha_feito'),
>>>>>>> cbaf1d1e81a58c4671f089b0910e966b481efa09

]
>>>>>>> parent of 3451a08... autenticacao  finalizada
