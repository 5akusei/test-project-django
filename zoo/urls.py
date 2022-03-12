from django.urls import path
from zoo.views import ListRecord
app_name = 'zoo'

urlpatterns = [
    path('', ListRecord.as_view(), name='home')
]