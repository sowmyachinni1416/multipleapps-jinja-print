from django.urls import path
from app1.views import *
app_name='jinja print'

urlpatterns=[
    path('jinja_print1/',jinja_print1,name='jinja_print1'),
]