from django.urls import path
from testApp.consumers import *


ws_patterns = [
    path('room/<str:name>', Users)
]