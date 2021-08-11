from django.shortcuts import render, redirect
from .forms.form_servico import ServicoForm
from .models import  Service


def cadastrar_servico(request):
    form=ServicoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('administracao:listar_servico')
        
    return render(request, 'servico/form_servico.html',{'form':form})

def lista_servico(request):
    context={}
    context['servicos']=Service.objects.all()
    return render(request, 'servico/listar_servico.html',context)

def editar_servico(request,id):

    servico=Service.objects.get(pk=id)
    form=ServicoForm(request.POST or None,instance=servico)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('administracao:listar_servico')
        
    return render(request, 'servico/form_servico.html',{'form':form})
    