from email.policy import default
import pdb
from pprint import pprint
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView
from tickets.forms import CalendarForm, PayInfoForm
from zones.models import Zone
from tickets.models import Ticket, TicketType
from django.http import JsonResponse
import json

class Index(ListView):
    queryset = TicketType.objects.order_by('created_at')
    template_name = 'ticket/index.html'
    context_object_name = 'records'

    # Validate user
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'GET':
                return super().dispatch(request, *args, **kwargs)
            elif request.method == 'POST':
                # pdb.set_trace()
                return JsonResponse(json.loads(request.body.decode('utf-8')))
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')

class CreateTicket(FormView):
    template_name = 'ticket/ticket_step01.html'
    context_object_name = 'form'
    form_class = CalendarForm
    
    # Validates
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'GET':
                return super().dispatch(request, *args, **kwargs)
            elif request.method == 'POST':
                zona = Zone.objects.get(id=self.kwargs.get('pk'))
                ticket = Ticket.objects.create(name='Pase para '+zona.name)
                ticket.zones.set([zona], through_defaults={'reserved_date': request.POST['reserved_date'], 'value':request.POST['value']})
                request.session['ticket_in_buy_process'] = ticket
                return redirect('ticket:pay_info')
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')

class UpdateTicket(UpdateView):
    template_name = 'ticket/ticket_step02.html'
    context_object_name = 'form'
    form_class = PayInfoForm
    
    # Validates
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Validacion del tiquete
            ticket = request.session.get('ticket_in_buy_process', None)
            if ticket is None:
                return redirect('ticket:index')
            
            # Validar metodos
            if request.method == 'GET':
                return super().dispatch(request, *args, **kwargs)
            elif request.method == 'POST':
                if request.POST['card_num'].isnumeric() and request.POST['CVC'].isnumeric():
                    # TODO: Actualizar el ticket
                    redirect('ticket:index')
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')