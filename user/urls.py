# from django import views
from django.urls import path
from user.views import CreateRecord, ListRecord, UpdateRecord, DeleteRecord
from django.contrib.auth.views import LogoutView
from . import views
from SpecialZoo import settings
app_name = 'user'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('registro', CreateRecord.as_view(), name='signup'),
    # path('cerrar-sesion/', views.logout, name='logout'),
    path('cerrar-sesion/', LogoutView.as_view(), name='logout'),
    path('lista', ListRecord.as_view(), name='list'),
    path('actualizar/<int:pk>', UpdateRecord.as_view(), name='update'),
    path('eliminar/<int:pk>', DeleteRecord.as_view(), name='delete'),
]