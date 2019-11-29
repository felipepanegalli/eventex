from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.model import Subscription


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


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name="Felipe Panegalli", cpf="12312312345", email="felipe.panegalli@gmail.com",
                    phone="12-12345-1234")
        self.response = self.client.post("/inscricao/", data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(self.response.status_code, 302)

    def test_send_subscribe_email(self):
        """Verify send email /inscricao/"""
        self.assertEqual(1, len(mail.outbox))

    def test_send_subscribe_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, email.subject)

    def test_send_subscribe_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, email.from_email)

    def test_send_subscribe_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'felipe.panegalli@gmail.com']
        self.assertEqual(expect, email.to)

    def test_send_subscribe_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Felipe Panegalli', email.body)
        self.assertIn('12312312345', email.body)
        self.assertIn('felipe.panegalli@gmail.com', email.body)
        self.assertIn('12-12345-1234', email.body)


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        self.response = self.client.post("/inscricao/", {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """"Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):
    def setUp(self):
        data = dict(name="Felipe Panegalli", cpf="12312312345", email="felipe.panegalli@gmail.com",
                    phone="12-12345-1234")
        self.response = self.client.post("/inscricao/", data, follow=True)

    def test_message(self):
        self.assertContains(self.response, 'Inscrição realizada com sucesso!')


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Felipe Panegalli',
            cpf='123,123,123-34',
            email='felipe.panegalli@gmail.com',
            phone='55-91234-1234'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())
