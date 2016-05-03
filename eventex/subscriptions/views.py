from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        #Pegar as informaçoes que vem através do POST no request
        #request.POST = dados da requisição
        form = SubscriptionForm(request.POST)
        #Processar os dados do formulário
        if form.is_valid():

            #Pegar o texto (corpo) da mensagem que está em subscriptions/subscription_email.txt
            #E passar os dados do formulário através do form.cleaned_data para
            #adicionar ao corpo da mensagem
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)

            #Enviar o email
            mail.send_mail('Confirmação de inscrição',
                           body,
                           'contato@eventex.com.br',
                           ['contato@eventex.com.br', form.cleaned_data['email']])
            #form.cleaned_data['email'] é o email que vem do formulário

            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})

    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
