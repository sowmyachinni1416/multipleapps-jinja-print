from django.urls import path
from app2.views import *
app_name='jinja print'

urlpatterns=[
    path('jinja_print2/',jinja_print2,name='jinja_print2'),
]