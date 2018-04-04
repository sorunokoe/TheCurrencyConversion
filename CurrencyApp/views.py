# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import View
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .models import Currencies, Rates
from .serializers import CurrenciesSerializer, RatesSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.core import serializers
#from TheCurrencyConversion.mails import mail_manager

from .tasks import fetchData

# Create your views here.
class IndexView(View):
    template_name = 'index.html'
    def get(self, request):

        #Need to delete after setting cron
        fetchData()

        return render(request, self.template_name)


# REST APIs
class CurrenciesApiView(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
class RatesApiView(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer