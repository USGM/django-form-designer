# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import form_designer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('form_designer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdefinition',
            name='reply_to',
            field=form_designer.fields.TemplateCharField(help_text=b'The reply-to header for the email, used if the sending email is not the email that should be replied to.', max_length=255, null=True, verbose_name='reply-to e-mail address', blank=True),
        ),
    ]