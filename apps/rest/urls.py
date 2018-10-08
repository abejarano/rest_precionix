from django.urls import path, include
from .views import *


urlpatterns = [
    path('price/<country>/', Price.as_view()),

]