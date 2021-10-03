from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.core.mail import  send_mail
from .models import  Usuario

def cadastrar_usuario(sender,instance,created,**kwargs):
    if created:
        assunto='Cadastro realizado com sucesso! '
        corpo='Mailgun'
        email_destino=[instance.email]
        email_remetente='leonardosaja87@gmail.com'
        mensagem_html=render_to_string('email_cadastro.html',{'usuario':instance})
        send_mail(assunto,corpo,email_remetente,email_destino,html_message=mensagem_html)

post_save.connect(cadastrar_usuario,sender=Usuario)