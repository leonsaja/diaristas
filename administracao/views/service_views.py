from django.shortcuts import render, redirect
from administracao.forms.form_servico import ServicoForm
from administracao.models import  Service
from django.contrib.auth.decorators import login_required
from django.core.mail import  send_mail
@login_required
def cadastrar_servico(request):
    form=ServicoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('administracao:listar_servico')
        
    return render(request, 'servico/form_servico.html',{'form':form})
@login_required
def listar_servicos(request):
    context={}
    context['servicos']=Service.objects.all()
    return render(request, 'servico/lista_servicos.html',context)
@login_required
def editar_servico(request,id):

    servico=Service.objects.get(pk=id)
    form=ServicoForm(request.POST or None,instance=servico)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('administracao:listar_servicos')
    return render(request, 'servico/form_servico.html',{'form':form})
    