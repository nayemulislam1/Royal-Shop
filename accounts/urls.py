from django.urls import path
from .views import sing_in, sing_up, forget_pass

urlpatterns = [
    path('singin/', sing_in, name="singin"),
    path('singup/', sing_up, name="singup"),
    path('forget_pass/', forget_pass, name="forget_pass"),
    
]
