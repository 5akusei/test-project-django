import pdb
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from user.forms import UserForm
from user.models import User

class CreateRecord(CreateView):
    template_name = 'user/sign_up.html'
    context_object_name = 'form'
    form_class = UserForm
    success_url = reverse_lazy('user:home')

    def form_valid(self, form):
        password = self.request.POST.get('password', None)
        conf_password = self.request.POST.get('conf_password', None)
        if password and conf_password:
            if password == conf_password:
                messages.success(self.request, 'Se guardo un usuario correctamente')
                return super().form_valid(form)
        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Los datos proporcionados son invalidos")
        return redirect('user:signup')

class ListRecord(ListView):
    queryset = User.objects.order_by('date_joined')
    template_name = 'user/list.html'
    context_object_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserForm
    
        return context

class UpdateRecord(UpdateView):
    template_name = 'user/update.html'
    model = User
    form_class = UserForm
    context_object_name = 'form'
    success_url = reverse_lazy('user:list')

    def form_valid(self, form):
        messages.success(self.request, "Actualizado correctamente")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.errro(self.request, "Error al actualizar")
        return redirect('user:update')

class DeleteRecord(DeleteView):
    model = User
    success_url = reverse_lazy('user:list')