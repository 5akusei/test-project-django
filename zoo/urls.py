from django.urls import path

from zoo.views import ListRecord

urlpatterns = [
    path('', ListRecord.as_view(), name='home')
]