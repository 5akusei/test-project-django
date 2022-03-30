from django.urls import path
from user.views import CreateRecord, ListRecord, UpdateRecord, DeleteRecord
app_name = 'user'

urlpatterns = [
    path('', CreateRecord.as_view(), name='signup'),
    path('lista', ListRecord.as_view(), name='list'),
    path('actualizar/<int:pk>', UpdateRecord.as_view(), name='update'),
    path('eliminar/<int:pk>', DeleteRecord.as_view(), name='delete'),
]