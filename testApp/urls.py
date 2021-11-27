from django.urls import path
from testApp.views import *

urlpatterns = [
    path('', home)
]