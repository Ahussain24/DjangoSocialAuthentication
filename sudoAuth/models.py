# Remove the content of the file in case of errors 

from django.contrib.auth.models import User
from django.db import models 

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
