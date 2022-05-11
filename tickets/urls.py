from django.urls import path
from tickets.views import Index
app_name = 'ticket'

urlpatterns = [
    path('', Index.as_view(), name='index'),
]