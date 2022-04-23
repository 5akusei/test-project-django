# from django import views
from django.urls import path
from user.views import CreateRecord, ListRecord, UpdateRecord, DeleteRecord, Index, CreateRecordWithEmailConfirm
from django.contrib.auth.views import LogoutView
from . import views
from SpecialZoo import settings
app_name = 'user'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('iniciar-sesion/', views.login_page, name='login'),
    path('cerrar-sesion/', LogoutView.as_view(), name='logout'),
    path('activar_usuario/<slug:uid>', views.activation_user, name='activate'),
    # path('cerrar-sesion/', views.logout, name='logout'),
    path('lista/', ListRecord.as_view(), name='list'),
    path('registro/', CreateRecordWithEmailConfirm.as_view(), name='signup'),
    path('eliminar/<int:pk>', DeleteRecord.as_view(), name='delete'),
    path('actualizar/<int:pk>', UpdateRecord.as_view(), name='update'),
]