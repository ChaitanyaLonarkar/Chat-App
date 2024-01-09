from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('mychatapp.urls')),
    path('', views.index,name='index'),
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page'),
    path('home/',views.home,name='home'),
    path('add_friend/',views.add_friend,name='add_friend'),
    path('friend_request/',views.friend_request,name='friend_request'),
    path('setting/',views.setting,name='setting'),
    path('notifications/',views.notifications,name='notifications'),
    path('home/chat/',views.chat,name='chat'),
    
]
