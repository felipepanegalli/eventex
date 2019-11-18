from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/inscricao/")

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_csrf(self):
        """"Html must contain csrftoken"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """"Context must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

    def test_html(self):
        """"Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="hidden"')
        self.assertContains(self.response, 'type="submit"')
