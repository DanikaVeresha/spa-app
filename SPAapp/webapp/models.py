from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100, null=False)
    Status = models.CharField(max_length=100, default="Registered")
    Email = models.EmailField(max_length=100, null=False)
    RegisterDate = models.DateTimeField(auto_now_add=True, null=False)
    HomePage = models.URLField(max_length=100, null=True)
    CAPTCHA = models.CharField(max_length=100, null=False, default="No CAPTCHA")
    Password = models.CharField(max_length=100, default="User does`t have a password")


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Created = models.DateTimeField(auto_now_add=True, null=True)
    Text = models.TextField(max_length=5000, null=False, default="No text")


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=100, null=False)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    Created = models.DateTimeField(auto_now_add=True, null=True)
    Text = models.TextField(max_length=5000, null=False, default="No text")
