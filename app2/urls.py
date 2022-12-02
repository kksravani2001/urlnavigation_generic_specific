from django.urls import path
from app2.views import *
app_name='aa'
urlpatterns=[
    path('ntr/',ntr,name='ntr'),
    path('happy/',happy,name='happy'),
]