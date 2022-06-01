from django.urls import path
from tickets.views import Index, CreateTicket
app_name = 'ticket'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('calendario/<int:pk>', CreateTicket.as_view(), name='calendar'),
    path('calendario/pago/<int:pk>', CreateTicket.as_view(), name='pay_info'),
]