from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash

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
            b = []
            if password:
                a = ['@', '#', '!', '$', '%', '&', '*']
                for i in a:
                    if i in password:
                        b.append(i)
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
                        messages.warning(request, "User Created !!!")
                        return redirect('singin')
                else:
                    messages.warning(request, "Password Not Match!!! ")
            else:
                messages.warning(request, "Enter a special character in password .")

    return render(request, 'accounts/singup.html')


def sing_in(request):
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

def forget_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            user = User.objects.get(email=email)
            if user.email == email:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'User password change successfully.')
                return redirect('singin')
            else:
                messages.error(request, 'email not matched.')

    return render(request, 'accounts/forget_password.html')

