from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method =="POST":
        if request.POST['password'] == request.POST['passwordCheck']:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request,'signup.html',{'error':"User has already taken"})
            except:
                user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"])
                auth.login(request,user)
                return redirect('/')
        else:
            return render(request,'signup.html',{'error':"Passwords must match"})
    else:
        return render(request,"signup.html")
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':"invalid username or password"})
    else:  
        return render(request,"login.html")
    
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("/")
    else:
        return render(request,'signup.html')