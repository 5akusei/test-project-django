import pdb
from pprint import pprint
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from user.forms import UserForm, UserFormUpdate, LoginForm
from user.models import User
from django.contrib.auth import login, logout, authenticate

class ListRecord(ListView):
    queryset = User.objects.order_by('date_joined')
    template_name = 'user/list.html'
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
        context['form'] = UserForm
    
        return context

class CreateRecord(CreateView):
    template_name = 'user/sign_up.html'
    context_object_name = 'form'
    form_class = UserForm
    # form_class = RegistrationForm
    success_url = reverse_lazy('zoo:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        
        return context

    def form_valid(self, form):
        password = self.request.POST.get('password', None)
        conf_password = self.request.POST.get('conf_password', None)
        if password and conf_password:
            if password == conf_password:
                # pdb.set_trace()
                # email = self.request.POST.get('email', None)
                # user_session = authenticate(email=email, password=password)
                user_instance = form.save()
                login(self.request, user_instance)
                messages.success(self.request, 'Registro exitoso')
                # return user_instance
                return super().form_valid(form)
        return super().form_invalid(form)

    def form_invalid(self, form):
        # pdb.set_trace()
        messages.error(self.request, "Los datos proporcionados son invalidos")
        return redirect('user:signup')

class UpdateRecord(UpdateView):
    template_name = 'user/update.html'
    model = User
    form_class = UserFormUpdate
    context_object_name = 'form'
    success_url = reverse_lazy('user:list')

    # Validate user
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # pdb.set_trace()
            if request.user.is_admin or request.user.id == self.kwargs.get('pk'):
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(request, 'No estas autorizado.')
                return redirect('user:index')    
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        
        return context

    def form_valid(self, form):
        messages.success(self.request, "Actualizado correctamente")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.errro(self.request, "Error al actualizar")
        return redirect('user:update')

class DeleteRecord(DeleteView):
    model = User
    success_url = reverse_lazy('user:list') 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(request, 'No estas autorizado.')
                return redirect('user:index')
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Sesión Cerrada')
        return redirect('user:login')

def login_page(request):
    form = LoginForm()
    message = ''
    context = {'form': form, 'message': message}
    # Validate user
    if request.user.is_authenticated:
        return redirect('user:index')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username = form.cleaned_data['email'],
                    password = form.cleaned_data['password'],
                )
                # pdb.set_trace()
                if user is not None:
                    login(request, user)
                    return redirect('user:index')
                message = 'Login failed!'
        return render(request, 'user/login.html', context)

class Index(TemplateView):
    template_name = 'user/index.html'

    # Validate user
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'GET':
                return super().dispatch(request, *args, **kwargs)
            elif request.method == 'POST':
                messages.error(request, 'Acción invalida. ¡Inicia Sesión!')
                return redirect('user:index')    
        else:
            messages.error(request, 'Por favor inicia sesión e intenta de nuevo.')
            return redirect('user:login')