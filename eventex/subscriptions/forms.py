from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('O CPF deve conter 11 números.')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Telefone')

    def clean_name(self):
        name = self.cleaned_data['name']
        name_capitalized = [w.capitalize() for w in name.split()]
        return ' '.join(name_capitalized)
