# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
from django_resized import ResizedImageField

import sys
if sys.version_info[0] == 3:
    from django.utils.encoding import smart_text as smart_unicode
else:
    from django.utils.encoding import smart_unicode


class Currencies(Model):

    code = CharField(max_length=3)
    description = CharField(max_length=100)
    rates = ManyToManyField('Rates', related_name="currency", blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.code)
    def __str__(self):
        return smart_unicode(self.code)

class Rates(Model):

    code = CharField(max_length=3)
    rate = FloatField()

    def __unicode__(self):
        return smart_unicode(self.code)
    def __str__(self):
        return smart_unicode(self.code)