from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('form', Form.as_view(), name='form'),
    path('edit/<int:pk>/', Edit.as_view(), name='edit'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete')
]