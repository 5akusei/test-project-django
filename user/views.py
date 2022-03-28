import pdb
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import UserForm

class CreateRecord(CreateView):
    template_name = 'user/sign_up.html'
    context_object_name = 'form'
    form_class = UserForm
    success_url = reverse_lazy('zoo:home')

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