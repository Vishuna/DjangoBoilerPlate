from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Register(models.Model):
    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50, null=True)
    username=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user",null=True)
    email_id=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.first_name

class Roles(models.Model):
    level_id=models.CharField(max_length=10, null=True)
    role_name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.role_name

class RolePermisson(models.Model):
    role_assign=models.ForeignKey(to=Roles, on_delete=models.CASCADE, related_name="rol2_assign", null=True)
    selected_staff=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="selected_staff", null=True)

    def __str__(self):
        return self.role_assign


