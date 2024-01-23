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
    path('update_profile/',views.update_profile,name='update_profile'),
    path('notifications/',views.notifications,name='notifications'),
    path('home/chat/',views.chat,name='chat'),
    path('logout/', views.logout_page,name='logout'),
    path('send_request/', views.send_friend_request,name='send_request'),
    path('accept_request/', views.accept_friend_request,name='accept_request'),
    
]
