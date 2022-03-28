from django.urls import path
from user.views import CreateRecord
app_name = 'user'

urlpatterns = [
    path('', CreateRecord.as_view(), name='signup'),
]