from django.db import models

# Create your models here.
class UserModel(models.Model):
    
    user_id = models.AutoField(primary_key=True,unique=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    password = models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    modified_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    role = models.CharField(max_length=13,null=True,blank=True,default='consumer')
