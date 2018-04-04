from django.contrib.auth.models import User
from rest_framework.serializers import *
from rest_framework.validators import UniqueValidator
from .models import Currencies, Rates


class CurrenciesSerializer(ModelSerializer):
    class Meta:
        model = Currencies
        fields = ('pk', 'code', 'description', 'rates')
class RatesSerializer(ModelSerializer):
    class Meta:
        model = Rates
        fields = ('pk', 'code', 'rate')