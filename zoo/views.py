from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zoo.forms import AnimalForm
from zoo.models import Animal

class ListRecord(ListView):
    queryset = Animal.objects.order_by('created_at')
    template_name = 'zoo/home.html'
    context_object_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnimalForm
    
        return context
        
class CreateRecord(CreateView):
    template_name = 'zoo/create.html'
    context_object_name = 'form'
    form_class = AnimalForm
    success_url = reverse_lazy('zoo:home')

    def form_valid(self, form):
        messages.success(self.request, 'Se guardo un animal correctamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Los datos proporcionados son invalidos")
        return redirect('zoo:home')

class ViewRecord(DetailView):
    template_name = 'zoo/detail.html'
    model = Animal
    context_object_name = 'record'

class UpdateRecord(UpdateView):
    template_name = 'zoo/update.html'
    model = Animal
    form_class = AnimalForm
    context_object_name = 'form'
    success_url = reverse_lazy('zoo:home')

    def form_valid(self, form):
        messages.success(self.request, "Actualizado correctamente")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.errro(self.request, "Error al actualizar")
        return redirect('zoo:update')

class DeleteRecord(DeleteView):
    model = Animal
    success_url = reverse_lazy('zoo:home')