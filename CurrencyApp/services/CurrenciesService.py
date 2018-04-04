
from CurrencyApp.models import Currencies, Rates
import requests

hostname = "https://openexchangerates.org/api"
app_id = "ea35e7adfd974e70b0a16e48e4a8e793"
base_codes = ['USD', 'CZK', 'EUR', 'PLN']

class CurrenciesService():

    all_codes = []
    all_description = []

    def getCurrencies(self, allcurrencies=None):
        if allcurrencies:
            for currency  in allcurrencies:
                if currency.code in base_codes:
                    self.getCurrenciesDescriptionAPI()
                    self.getRates(currency)
        else:
            self.getCurrenciesDescriptionAPI()
            self.getRates()

    def getRates(self, currency=Currencies()):

        for code in base_codes:

            # Can't get all currencies, because 'based' parameter not for free of charge.
            #     response = requests.get(hostname + "/latest.json?app_id=" + app_id+"&based="+code)
            if code == 'USD':
                response = requests.get(hostname + "/latest.json?app_id=" + app_id)
                json = response.json()
                self.all_rates = json['rates']
                if not currency.code:
                    currency.code = code
                if not currency.description:
                    currency.description = self.all_description[code]
                currency.save()
                currency_rates = []
                for code2 in base_codes:
                    if code2 in self.all_rates.keys():
                        if code != code2:
                            rate = None
                            if code == currency.code:
                                for currency_rate in currency.rates.all():
                                    if code2 == currency_rate.code:
                                        rate = currency_rate
                            if rate == None:
                                rate = Rates()
                                rate.code = code2
                            rate.rate = self.all_rates[code2]
                            rate.save()
                            currency_rates.append(rate)
                currency.rates = currency_rates
                currency.save()


    def getCurrenciesDescriptionAPI(self):
        response = requests.get(hostname+"/currencies.json")
        json = response.json()
        for code in base_codes:
            if code in json.keys():
                print(code)
                print(json[code])
        self.all_description = json







