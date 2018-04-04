app_name = 'landing'
from django.conf.urls import url, include
from CurrencyApp import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
router = routers.SimpleRouter()


router = routers.SimpleRouter()
router.register(r'currencies', views.CurrenciesApiView)
router.register(r'rates', views.RatesApiView)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
]

urlpatterns = format_suffix_patterns(urlpatterns)