from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
import json
from mychatapp.form import UserProfileForm
from .models import Profile,FriendRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request,'index.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home')
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
    if request.user.is_authenticated:
        return redirect('/home')
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
    all_user=get_user_model()
    # all_user= User.objects.all()
    profile, created = Profile.objects.get_or_create(user = request.user)
    profile_friends=profile.friends.all()
    suggested_friends= all_user.objects.exclude(userprofile__friends__in = profile_friends).exclude(userprofile = profile)
    
    # friend_requests=FriendRequest.objects.filter(receiver__in=suggested_friends,sender=request.user).first()
    friend_requests=FriendRequest.objects.filter(receiver__in=suggested_friends,sender=request.user)
    
    # print(friend_requests)
    context={"s_friends":suggested_friends,"f_friends":friend_requests}
    return render(request,'add_friend.html',context)

@login_required(login_url='/login')
def friend_request(request):
    user=request.user
    friend_request=FriendRequest.objects.filter(receiver=user)
    context={"f_friends":friend_request}
    return render(request,'friend_request.html',context)

@login_required(login_url='/login')
def update_profile(request):
    # user=request.user
    # print(user)
    # profile=Profile.objects.get(user=user)
    # print(profile)
    # form = UserProfileForm(instance=profile)
    # profile, created = Profile.objects.get_or_create(user=request.user)
    
    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST, request.FILES, instance=profile)

    #     if form.is_valid():
    #         form.save()
    #         return redirect('update_profile')  # Redirect to the same page after successful update
    # else:
    #     form = UserProfileForm(instance=profile)
        
    # context={'form':form}
    
    profile, created = Profile.objects.get_or_create(user=request.user)
    # print(profile)
    if request.method == 'POST':
        profile.username=request.POST.get('username')
        profile.first_name=request.POST.get('firstname')
        profile.last_name=request.POST.get('lastname')
        profile.profile_picture=request.POST.get('profile_picture')
        profile.save()
        return redirect('update_profile')  
    return render(request,'update.html')


@login_required(login_url='/login')
def chat(request):
    return render(request,'chat.html')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def send_friend_request(request):
    data =json.loads(request.body)
    user=get_user_model()
    receiver=user.objects.get(id=data)
    friend_request=FriendRequest.objects.create(sender=request.user,receiver=receiver)
    return JsonResponse('chat',safe=False)

# @login_required(login_url='/login')
def accept_friend_request(request):
    data =json.loads(request.body)
    user=get_user_model()
    n_user=user.objects.get(id=data)
    profile=Profile.objects.get(user_id=request.user.id)
    msg=None
    profile2=Profile.objects.get(user_id=data)
    if profile:
        if profile.friends.filter(id=data).exists():
            profile.friends.remove(n_user)
            msg="no"
        else:
            profile.friends.add(n_user)
            msg="yes"
            
    if profile2:
        if profile2.friends.filter(id=request.user.id).exists():
            profile2.friends.remove(request.user)
        else:
            profile2.friends.add(request.user)
    return JsonResponse(msg,safe=False)