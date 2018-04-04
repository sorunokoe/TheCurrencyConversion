
from .models import Currencies, Rates
from CurrencyApp.services.CurrenciesService import CurrenciesService

from celery.schedules import crontab
from celery.task import periodic_task

@periodic_task(run_every=crontab(hour=0, minute=0))
def fetchData():
    allcurrencies = Currencies.objects.all()
    service = CurrenciesService()
    if allcurrencies:
        service.getCurrencies(allcurrencies)
    else:
        service.getCurrencies()