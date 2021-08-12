from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from ..forms.form_usuario import CadastroUsuarioForms,EditarUsuarioForm
from django.contrib.auth import get_user_model, authenticate, login, logout


def login_usuario(request):

    form = AuthenticationForm(request.POST or None)

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('administracao:listar_servicos')
        else:
            User=get_user_model()
            if not User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Usuário não existe  ')
            else:
                messages.add_message(request, messages.ERROR, 'Usuário ou Senha inválida  ')
    return render(request, 'registration/login.html', {'form': form})

def deslogar_usuario(request):
    logout(request)
    return redirect('administracao:login_usuario')

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