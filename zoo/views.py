from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from zoo.forms import AnimalForm

from zoo.models import Animal

class ListRecord(ListView):
    queryset = Animal.objects.order_by('create_at')
    template_name = 'zoo/home.html'
    context_object_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnimalForm
    
        return context
        
