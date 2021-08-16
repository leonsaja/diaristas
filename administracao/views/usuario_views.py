from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.template.loader import render_to_string

from ediaristas import settings
from ..forms.form_usuario import CadastroUsuarioForms,EditarUsuarioForm
from django.contrib.auth import  get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar_usuario(request):
    form = CadastroUsuarioForms()
    if request.method=='POST':
        form = CadastroUsuarioForms(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('administracao:listar_usuarios')


    return render(request,'usuario/form_usuario.html',{'form':form})

@login_required
def listar_usuarios(request):
    User=get_user_model()
    usuarios=User.objects.all()
    return render(request,'usuario/lista_usuarios.html',{'usuarios':usuarios})
@login_required
def editar_usuario(request,id):
    User=get_user_model()
    usuario=User.objects.get(id=id)
    form=EditarUsuarioForm(request.POST or None,instance=usuario)

    if form.is_valid():
            form.save()
            redirect('administracao:listar_usuarios')
    return render(request,'usuario/editar_usuario.html', {'form': form})

def user_info(request,id):
    User = get_user_model()
    usuario = User.objects.get(id=id)

    return render(request,'usuario/lista_id_usuario.html',{'usuario':usuario})

def enviar_email(request,id):
    User=get_user_model()
    usuario=User.objects.get(id=id)
    assunto='Resumo do Usuario'
    print(usuario)
    html_conteudo=render_to_string('usuario/lista_id_usuario.html',{'usuario':usuario},request)
    corpo_email='Dados cadastrado'
    email_remente=settings.EMAIL_HOST_USER
    email_destino=[usuario.email]
    print('teste',email_destino)
    send_mail(assunto,corpo_email,email_remente,email_destino,html_message=html_conteudo)
    return redirect('administracao:listar_usuarios')


