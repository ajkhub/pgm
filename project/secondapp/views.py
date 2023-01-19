from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['f1']
        password = request.POST['f2']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credential")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['f1']
        firstname = request.POST['f2']
        lastname = request.POST['f3']
        email = request.POST['f4']
        password = request.POST['f5']
        cpassword = request.POST['f6']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"E-mail Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname,email=email)
                user.save();
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"Password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

