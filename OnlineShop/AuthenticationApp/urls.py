from django.urls import path
from AuthenticationApp.views import Register, close_session, log

urlpatterns = [
    path('', Register.as_view(), name='authentication'),
    path('close_session/', close_session, name='close_session'),
    path('login/', log, name='login'),
]
