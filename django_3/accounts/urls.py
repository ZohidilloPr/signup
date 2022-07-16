from django.urls import path
from .views import CreateUser, Login, LogOut

app_name = 'accounts'

urlpatterns = [
    path("signup/", CreateUser, name="CU"),
    path("login/", Login, name="LI"),
    path("logout/", LogOut, name="LO"),
]
