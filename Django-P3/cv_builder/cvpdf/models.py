from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    address = models.TextField()
    school = models.TextField()
    university = models.TextField()
    degree = models.CharField(max_length=300)
    experience = models.CharField(max_length=300)
    summary = models.TextField(blank=True, null=True)
    social_link = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/',  blank=True, null=True , default='profiles/default.png')


    def __str__(self):
        return self.full_name 
