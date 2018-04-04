# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Currencies, Rates

from django.contrib import admin

# Register your models here.
admin.site.register(Currencies)
admin.site.register(Rates)



