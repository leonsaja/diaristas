from django.shortcuts import render,redirect
from ..forms.form_usuario import UsuarioForms
from django.contrib.auth import get_user_model

def cadastrar_usuario(request):
    form = UsuarioForms()
    if request.method=='POST':
        form = UsuarioForms(request.POST or None)
        if form.is_valid():
            form.save()
            redirect('administracao:lista_usuarios')


    return render(request,'usuario/form_usuario.html',{'form':form})


def listar_usuarios(request):
    User=get_user_model()
    usuarios=User.objects.all()
    return render(request,'usuario/lista_usuarios.html',{'usuarios':usuarios})