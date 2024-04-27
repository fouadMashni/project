from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User

from django.contrib import messages





# Create your views here.

def Login (request) : 
    return render(request , "app/Login.html")
def Register(request) :
    return render (request , "app/Register.html")

def Course (request) :
   return render(request , "app/Course.html")

def Search (request) :
   return render(request , "app/Search.html")

def Course_details(request) :
   return render(request,"app/Course_details.html")

def main(request):
   return render (request,"app/main.html")

def dashboard(request) :
   return render (request,"app/dashboard.html")


def logout(request):
    
    return redirect('main')


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('new_password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('Register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect('LogIn')
    return render(request, 'app/Register.html')




def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('LogIn')
    return render(request, 'app/Login.html')



