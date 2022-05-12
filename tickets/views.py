from django.views.generic import ListView
from zones.models import Zone
from django.contrib import messages
from django.shortcuts import redirect

class Index(ListView):
    queryset = Zone.objects.order_by('created_at')
    template_name = 'ticket/index.html'
    context_object_name = 'records'

    # Validate user
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'GET':
                return super().dispatch(request, *args, **kwargs)
            elif request.method == 'POST':
                messages.error(request, 'Acción invalida.')
                return redirect('user:login')    
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context