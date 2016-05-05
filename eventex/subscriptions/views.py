from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm

def subscribe(request):
    # Pegar as informaçoes que vem através do POST no request
    # request.POST = dados da requisição
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = SubscriptionForm(request.POST)

    #Processar os dados do formulário
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    #Pegar o texto (corpo) da mensagem que está em subscriptions/subscription_email.txt
    #E passar os dados do formulário através do form.cleaned_data para
    #adicionar ao corpo da mensagem e enviar por e-mail
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email'],
               'subscriptions/subscription_email.txt',
               form.cleaned_data)
    # form.cleaned_data['email'] é o email que vem do formulário
    #settings.DEFAULT_FROM_EMAIL: é uma configuração do Django que permite enviar um email
    #com um email de remetente definido no settings.py dentro de eventex

    #Feedback de sucesso
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')

def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})

#Curiosidade: em Python não existe público e privado, tudo é público
def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    # Enviar o email
    mail.send_mail(subject, body, from_, [from_, to])