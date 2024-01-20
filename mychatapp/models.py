from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
    username= models.CharField(max_length=50,blank=True,null=True)
    first_name= models.CharField(max_length=50,blank=True,null=True)
    last_name= models.CharField(max_length=50,blank=True,null=True)
    username= models.CharField(max_length=50,blank=True,null=True)
    profile_picture=models.ImageField(upload_to='img',blank=True,null=True)
    friends=models.ManyToManyField(User,blank=True,related_name='user_friends')
    
    def __str__(self):
        return self.username
    
class FriendRequest(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sent_request")
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name="receive_request")
    seen=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.sender.username} sent {self.receiver.username} a friend request"