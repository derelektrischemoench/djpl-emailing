# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from django.core import mail
from django.test import TestCase, override_settings
from emailing import emails
from django_productline.testingutils import NoMigrationsTestCase
from premailer import transform
from emailing import emails
from emailing.emails import HtmlEmail

import settings


# explicitely introduce global email settings here, that other features
# are able to use refinements consistently (from a django perspective this seems redundant)


def test_send_email():
    context = dict(
        brand_bg='#fff',
        body_bg='#eee',
        brand_color='#575757',
        link_color='#2244DD',
        footer_content='Welcome, this is a mail',
    )

    msg = HtmlEmail(
        subject='test',
        template='test_signup.html',
        context=context,
        to=['chris.bader@schnapptack.de', ]
    )
    msg.content_subtype = 'html'
    msg.send(fail_silently=False)

if __name__ == "__main__":
    test_send_email()
