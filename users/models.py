from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length= 200,null=True,blank=True)

    user_name=models.CharField(max_length= 200,null=True,blank=True)
    location=models.CharField(max_length= 200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    short_intro=models.CharField(max_length= 200,null=True,blank=True)
    bio= models.TextField(blank=True,null=True)
    profile_image =  models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github=models.CharField(max_length= 200,null=True,blank=True)
    social_twitter=models.CharField(max_length= 200,null=True,blank=True)
    social_linkedin=models.CharField(max_length= 200,null=True,blank=True)
    social_youtube=models.CharField(max_length= 200,null=True,blank=True)
    social_website=models.CharField(max_length= 200,null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)


    def __str__(self):
        return str(self.user_name)

class Skill(models.Model):
    owner=models.ForeignKey(profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length= 200,null=True,blank=True)
    description= models.TextField(blank=True,null=True)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)


    def __str__(self):
        return str(self.name)


class Message(models.Model):
    sender= models.ForeignKey(profile,on_delete=models.SET_NULL,null=True,blank=True)
    recipient= models.ForeignKey(profile,on_delete=models.SET_NULL,null=True,blank=True,related_name="messages")
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False,null=True)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)


    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read','-created']

    


    
