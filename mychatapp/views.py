from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def notifications(request):
    return render(request,'notifications.html')

def add_friend(request):
    return render(request,'add_friend.html')

def friend_request(request):
    return render(request,'friend_request.html')

def setting(request):
    return render(request,'update.html')

def chat(request):
    return render(request,'chat.html')