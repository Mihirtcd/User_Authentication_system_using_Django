from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    
# def loginUser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         #check if user has entered correct credentials
#         user=authenticate(username=username,password=password)
#         if user is not None:
#     # A backend authenticated the credentials
#             login(request, user)
#             return redirect('/')
#         else:
#     # No backend authenticated the credentials
#             return render(request,'login.html')
#     return render(request,'login.html')
from django.contrib import messages  # Import messages framework

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')  # Send an error message
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
# def loginUser(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print("Debug: Username:", username)  # Debug output
#         print("Debug: Password:", password)  # Debug output

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             print("Debug: Authentication failed")  # More detailed debug output
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")