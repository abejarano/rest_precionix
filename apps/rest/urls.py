from django.urls import path, include
from .views import *


urlpatterns = [
    path('price/', Price.as_view()),

]