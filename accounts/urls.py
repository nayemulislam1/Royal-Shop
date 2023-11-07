from django.urls import path
from .views import log_in, verify_email, sing_up, forget_pass, verify_otp, log_out, confirm_pass, my_account

urlpatterns = [
    path('singin/', log_in, name="log_in"),
    path('singup/', sing_up, name="singup"),
    path('verify_email/', verify_email, name="verify_email"),
    path('sing_out/', log_out, name="log_out"),
    path('forget_pass/', forget_pass, name="forget_pass"),
    path('verify_otp/', verify_otp, name="verify_otp"),
    
    path('confirm_pass/', confirm_pass, name="confirm_pass"),
    path('my_account/', my_account, name="my_account"),
]
