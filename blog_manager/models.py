from django.db import models

# Create your models here.
class BlogModel(models.Model):
    
    user_id = models.IntegerField(null=True,blank=True)
    blog_id = models.AutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=150,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    content = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    is_draft = models.BooleanField(default=False,null=True,blank=True)

class LikeModel(models.Model):
    
    user_id = models.IntegerField(null=True,blank=True)
    blog_id = models.IntegerField()
    like_id = models.AutoField(primary_key=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    
    