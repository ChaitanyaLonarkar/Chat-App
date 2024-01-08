from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('mychatapp.urls')),
    path('', views.index),
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page'),
    
    
]
