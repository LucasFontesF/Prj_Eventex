from django.core import mail
from django.test import TestCase
# biblioteca para envio de emails: from django.core import mail

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Lucas Fontes', cpf='12345678901',
                    email='lucas@fontes.net', phone='11-91234-5678')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'lucas@fontes.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        # adicionar os dados no formulário
        contents = ['Lucas Fontes',
                    '12345678901',
                    'lucas@fontes.net',
                    '11-91234-5678']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)