from django.urls import path
from .views import view_message

urlpatterns = [
    path('', view_message, name='message'),
]
