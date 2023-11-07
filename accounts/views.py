from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash

from django.conf import settings
from django.core.mail import send_mail
import random
from .models import Profile

# Create your views here.
def sing_up(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if len(password) == 0 and len(password1) == 0:
            messages.warning(request, "Input Password !!!")
        elif len(password) < 4:
            messages.warning(request, "Enter Password At-least 4 Character !!!")
        elif len(username) == 0:
            messages.warning(request, "Input Username !!!")
        elif len(username) < 4:
            messages.warning(request, "Enter Username At-least 4 Character !!!")
        elif len(email) == 0:
            messages.warning(request, "Input Email !!!")

        else:
            if password:
                a = []
                b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                c = []
                d = ['&', '$', '#', '@', '*', '!', '_', '/', '-']
                for i in b:
                    if i in password:
                        a.append(i)
                for i in d:
                    if i in password:
                        c.append(i)
            if len(b) != 0:
                if password == password1:
                    if User.objects.filter(username=username).exists():
                        messages.warning(request, "Username Already Taken !!!")
                    elif User.objects.filter(email=email).exists():
                        messages.warning(request, "Email Already Taken !!!")
                    else:
                        user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password )
                        user.set_password(password)
                        user.save()
                        messages.warning(request, "Profile Created !!!")
                        return redirect('log_in')
                else:
                    messages.warning(request, "Password Not Match!!! ")
            else:
                messages.warning(request, "enter minimum 1 number and 1 special character in your password .")

    return render(request, 'accounts/singup.html')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST': 
        username = request.POST['name']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "User Logged in.")
            return redirect('home')
        else:
            messages.warning(request, "Create User First !!!")
            return redirect('singup')

    return render(request, 'accounts/singin.html')


def verify_email(r):
    pass

def forget_pass(request):
    otp = random.randint(1111, 9999)
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            if email:
                send_mail_registration(email, otp)
                user = User.objects.get(email=email)
                if user:
                    try:
                        prof = Profile.objects.get(user=user)
                        if prof:
                            prof.otp = otp
                            prof.save()
                            return redirect('verify_otp')
                    except:
                        prof = Profile.objects.create(user=user, otp=otp)
                        prof.save()
                        return redirect('verify_otp')
        except:
            messages.warning(request, "User Not Found.")
            return redirect('forget_pass')

    return render(request, 'accounts/forget_password.html')

# def forget_password(request):
#     # otp = random.randint(1111, 9999)
#     otp = int(time.strftime("%H%S%M")) + int(time.strftime("%S"))
#     if request.method == "POST":
#         email = request.POST.get('email')
#         user_obj = User.objects.filter(email=email).first()
#         pro_obj = Profile.objects.filter(user=user_obj).first()
#         if user_obj:
#             pro_obj.otp = otp
#             pro_obj.save()
#             send_otp(email, otp)
#             request.session['email'] = request.POST['email']
#             messages.success(request, "You OTP is send on your Email. Please Check Out.")
#             return redirect('Enter_otp')
#         else:
#             messages.error(request, "Invalid Email, Please Enter Correct Email.")
#     return render(request, "Auth/ForgetPass/forget_password.html")

# def Enter_otp(request):
#     email = request.session['email']
#     if request.session.has_key('email'):
#         user_obj = User.objects.filter(email=email).first()
#         pro_obj = Profile.objects.filter(user=user_obj).first()
#         if request.method == "POST":
#             otp_u = request.POST.get('otp')

#             if not otp_u:
#                 messages.error(request, "OTP is Required.")
#                 return redirect('Enter_otp')
#             elif int(pro_obj.otp) == int(otp_u):
#                 messages.success(request, "Set New Password.")
#                 return redirect('password_reset')
#             else:
#                 messages.error(request, "OTP is Invalid.")
#                 return redirect('Enter_otp')
#     else:
#         return redirect('forget_password')
#     return render(request, "Auth/ForgetPass/enter_otp.html")

def verify_otp(r):
    if r.method == 'POST':
        email = r.POST.get('email')
        password = r.POST.get('pass')
        otp = r.POST.get('otp')
        if email:
            user = User.objects.get(email=email)
            if user:
                prof = Profile.objects.get(user=user)
                if prof.otp == otp:
                    user.set_password(password)
                    user.save()
                    update_session_auth_hash(r, user)
                    messages.warning(r, "User Password Changed.")
                    return redirect('log_in')
                else:
                    messages.warning(r, "Otp not matched Try again.")
            else:
                messages.warning(r, "by the email no user found.")
                return redirect('forget_pass')
    return render(r, 'accounts/verify_otp.html')


def confirm_pass(r):

    return render(r, 'accounts/home.html')

def send_mail_registration(email, otp):
    subject = "Account Verification otp"
    message = f'hi your verify otp is :  {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def log_out(request):
    auth.logout(request)
    return redirect('log_in')




def my_account(r):
    
    return render(r, 'accounts/my_account.html')
