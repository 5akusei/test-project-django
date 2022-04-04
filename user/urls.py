# from django import views
from django.urls import path
from user.views import CreateRecord, ListRecord, UpdateRecord, DeleteRecord
from . import views
app_name = 'user'

urlpatterns = [
    path('', CreateRecord.as_view(), name='signup'),
    path('cerrar-sesion/', views.logout, name='logout'),
    path('lista', ListRecord.as_view(), name='list'),
    path('actualizar/<int:pk>', UpdateRecord.as_view(), name='update'),
    path('eliminar/<int:pk>', DeleteRecord.as_view(), name='delete'),
]