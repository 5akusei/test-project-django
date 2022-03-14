from django.urls import path
from zoo.views import CreateRecord, ListRecord, ViewRecord
app_name = 'zoo'

urlpatterns = [
    path('', ListRecord.as_view(), name='home'),
    path('detalle/<int:pk>', ViewRecord.as_view(), name='detail'),
    path('crear/', CreateRecord.as_view(), name='create'),
    path('editar/<int:pk>', ListRecord.as_view(), name='update'),
    path('eliminar/<int:pk>', ListRecord.as_view(), name='delete')
]