from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    # Verifications if form is valid
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    # Send email
    _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, form.cleaned_data['email'],
               'subscriptions/subscription_email.txt', form.cleaned_data)

    # Success feedback
    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def new(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
