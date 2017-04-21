import unittest
from django.core import mail
from django.test import TestCase, override_settings
from emailing import emails
from emailing.emails import HtmlEmail
from django_productline.testingutils import NoMigrationsTestCase
from premailer import transform
from emailing.emails import send


class SignupMailTest(NoMigrationsTestCase):
    """
    This is a helper test class which allows us to programmatically send emails for proper viewing
    """
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def test_send_email(self, **kwargs):
        from django.conf import settings
        context = dict(
            brand_bg='#fff',
            body_bg='#eee',
            brand_color='#575757',
            link_color='#2244DD',
            footer_content='Welcome, this is a mail',
            username=kwargs.pop('username')
        )

        msg = HtmlEmail(
            subject='test',
            template='test_signup.html',
            context=context,
            to=['chris.bader@schnapptack.de', ]
        )
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)

