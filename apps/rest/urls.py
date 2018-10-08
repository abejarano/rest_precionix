from django.urls import path, include
from .views import *


urlpatterns = [
    path('price/locale/', Price_locale.as_view()),
    path('price/<country>/', Price.as_view()),


]