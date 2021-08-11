from django.shortcuts import render,redirect
from ..forms.form_usuario import UsuarioForms


def cadastrar_usuario(request):
    form = UsuarioForms()
    if request.method=='POST':
        form = UsuarioForms(request.POST or None)
        if form.is_valid():
            form.save()


    return render(request,'usuario/form_usuario.html',{'form':form})


def listar_usuario(self):

    pass