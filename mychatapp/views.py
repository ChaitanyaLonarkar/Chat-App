from django.shortcuts import render,redirect
from django.contrib import messages
# from home.models import 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        #checking that the user having exists in table (
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login')
        
        # to authenticate username and passward then it create object and check the password is matching or not with the user input
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('/login')

        else: 
            login(request,user)
            return redirect('/home')
    return render(request,'login.html')

def register_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')

        # checking if the user is already registerd 
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username is already taken.")
            return redirect('/register')

        user=User.objects.create(first_name=first_name,last_name=last_name,username=username)

        #to make incripted passward otherwise give to above object  as an argument passward=passward
        user.set_password(password) 
        user.save()
        # print(username,password, first_name,last_name)
        messages.add_message(request, messages.INFO, "User Registered Successfully.")
    return render(request,'register.html')

@login_required(login_url='/login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='/login')
def notifications(request):
    return render(request,'notifications.html')

@login_required(login_url='/login')
def add_friend(request):
    return render(request,'add_friend.html')

@login_required(login_url='/login')
def friend_request(request):
    return render(request,'friend_request.html')

@login_required(login_url='/login')
def setting(request):
    return render(request,'update.html')

@login_required(login_url='/login')
def chat(request):
    return render(request,'chat.html')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')