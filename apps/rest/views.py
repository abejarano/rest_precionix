import decimal
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from price_onixcoin.models import PriceOnix

class Price(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data_onix = PriceOnix.objects.all()[:1]
        data_onix = data_onix[0]
        print(data_onix)

        return Response({
            'btc_onx_buy': '{:f}'.format(data_onix.btc_onx_buy),
            'onx_bs_buy':data_onix.onx_bs_buy,
            'usd_onx_buy':data_onix.usd_onx_buy,
            'btc_onx_sell':'{:f}'.format(data_onix.btc_onx_sell),
            'onx_bs_sell':data_onix.onx_bs_sell,
            'usd_onx_sell':data_onix.usd_onx_sell
        })