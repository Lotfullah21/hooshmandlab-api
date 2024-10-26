from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="student_profile")
    profile_picture = models.ImageField(upload_to="profiles/student", null=True, blank=True, )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name if self.user.first_name and self.user.last_name else self.user.username
    
    
class Instructor(models.Model):
    CHOICES = (("artificial-intelligence","Artificial Intelligence"),("python-programming","Python Programming"),("web-development","Web Development"))
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= "instructor_profile")
    profile_picture = models.ImageField(upload_to="profiles/instructors", null=True, blank=True)
    phone_number = models.CharField(max_length = 15, null=True, blank=True)
    expertise = models.CharField(max_length=255, choices =CHOICES ,blank=True, null=True)  
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name if self.user.first_name and self.user.last_name else self.user.username