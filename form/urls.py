from django.urls import path
from .views import *

urlpatterns = [
    path('formlist/', FormList.as_view(), name='form-list'),
    path('formcreate/', FormCreate.as_view(), name='form-create')
]
