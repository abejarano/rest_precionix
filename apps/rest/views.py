import decimal
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from price_onixcoin.models import PriceOnix, Country


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Price(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, country):
        if len(country) == 0:
            return Response({'not country'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        data_onix = PriceOnix.objects.filter(country=Country.objects.get(code_country=country))[:1]
        data_onix = data_onix[0]

        return Response({
            'btc_onx_buy': '{:f}'.format(data_onix.btc_onx_buy),
            'onx_bs_buy':data_onix.onx_bs_buy,
            'usd_onx_buy':data_onix.usd_onx_buy,
            'btc_onx_sell':'{:f}'.format(data_onix.btc_onx_sell),
            'onx_bs_sell':data_onix.onx_bs_sell,
            'usd_onx_sell':data_onix.usd_onx_sell
        })

class Price_locale(APIView):
    permission_classes = (AllowAny,)


    def get(self, request):
        from django.contrib.gis.geoip2 import GeoIP2

        ip = get_client_ip(request)
        if ip == '127.0.0.1':
            ip = '200.35.194.69'

        g = GeoIP2()
        country = g.country(ip)

        pais = Country.objects.get(country=country['country_name'])


        data_onix = PriceOnix.objects.filter(country=pais)[:1]
        data_onix = data_onix[0]

        return Response({
            'btc_onx_buy': '{:f}'.format(data_onix.btc_onx_buy),
            'onx_local_buy': data_onix.onx_bs_buy,
            'usd_onx_buy': data_onix.usd_onx_buy,
            'btc_onx_sell': '{:f}'.format(data_onix.btc_onx_sell),
            'onx_local_sell': data_onix.onx_bs_sell,
            'usd_onx_sell': data_onix.usd_onx_sell,
            'country': pais.country,
            'code_currency': pais.code_currency
        })
