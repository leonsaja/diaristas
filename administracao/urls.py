from django.urls import path, reverse_lazy
from .views.service_views import cadastrar_servico,listar_servicos,editar_servico
from .views.usuario_views import cadastrar_usuario,listar_usuarios,editar_usuario,enviar_email,user_info
from django.contrib.auth import views as auth_views

app_name='administracao'

urlpatterns = [

    #servico
    path('servicos/cadastrar/',cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar',listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>',editar_servico, name='editar_servico'),

   #Usuario
   path('usuario/cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
   path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
   path('usuario/editar/<int:id>', editar_usuario, name='editar_usuario'),
   path('usuario/listar_id/<int:id>', user_info, name='info_user'),
   path('usuario/enviar_email/<int:id>', enviar_email, name='enviar_email'),

   #autenticacao
   path('autenticacao/login', auth_views.LoginView.as_view(),name='login_usuario'),
   path('autenticacao/logout', auth_views.LogoutView.as_view(),name='deslogar_usuario'),

   path('alterar_senha', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('administracao:listar_servicos')), name='alterar_senha'),
   path('resetar_senha',auth_views.PasswordResetView.as_view(success_url=reverse_lazy('administracao:password_reset_done')),name='resetar_senha'),
   path('resetar_senha/sucesso',auth_views.PasswordResetCompleteView.as_view(), name='resetar_senha_sucesso'),
   path('resetar_senha/<str:uidb64>/<str:token>',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('administracao:resetar_senha_sucesso')),name='password_reset_confirm'),
   path('resetar_senha/feito',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

]
