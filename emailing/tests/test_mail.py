import unittest
from django.core import mail
from django.test import TestCase, override_settings
from emailing import emails
from emailing.emails import HtmlEmail
from django_productline.testingutils import NoMigrationsTestCase


class SignupMailTest(NoMigrationsTestCase):
    """
    This is a helper test class which allows us to programmatically send emails for proper viewing
    """

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def test_send_email(self):
        from django.conf import settings
        context = dict(
            brand_bg='#fff',
            body_bg='#eee',
            brand_color='#575757',
            link_color='#2244DD',
            footer_content='Welcome, this is a mail'
        )

        msg = HtmlEmail(
            subject='test',
            template='new_email/index.html',
            context=context,
            to=['chris.bader@schnapptack.de',
                'baederchris@gmail.com',
                'chris_bader@gmx.net']
        )
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)

        #self.assertEqual(len(mail.outbox), 1)
        #self.assertEqual(mail.outbox[0].subject, "Subject")
