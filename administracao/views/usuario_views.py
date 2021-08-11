from django.shortcuts import render,redirect
from ..forms.form_usuario import CadastroUsuarioForms,EditarUsuarioForm
from django.contrib.auth import get_user_model

def cadastrar_usuario(request):
    form = CadastroUsuarioForms()
    if request.method=='POST':
        form = CadastroUsuarioForms(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('administracao:listar_usuarios')


    return render(request,'usuario/form_usuario.html',{'form':form})


def listar_usuarios(request):
    User=get_user_model()
    usuarios=User.objects.all()
    return render(request,'usuario/lista_usuarios.html',{'usuarios':usuarios})

def editar_usuario(request,id):
    User=get_user_model()
    usuario=User.objects.get(id=id)
    form=EditarUsuarioForm(request.POST or None,instance=usuario)

    if form.is_valid():
            form.save()
            redirect('administracao:listar_usuarios')
    return render(request,'usuario/editar_usuario.html', {'form': form})