from django.urls import path
from .views import ViewMessage

urlpatterns = [
    path('', ViewMessage.as_view(), name='message'),
]
