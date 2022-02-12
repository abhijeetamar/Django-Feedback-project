from django.urls import path
from testapp.views import *

urlpatterns=[
    path('',feedback_view)
]