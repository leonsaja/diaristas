from django.shortcuts import render,redirect
from ..forms.form_usuario import CadastroUsuarioForms,EditarUsuarioForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required


@login_required
=======
from django.contrib.auth import get_user_model

>>>>>>> parent of 3451a08... autenticacao  finalizada
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