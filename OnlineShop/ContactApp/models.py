from django.db import models

# Create your models here.

class Contact(models.Model):
    
    c_name = models.CharField(max_length=50, null=False, blank=False)
    c_email = models.EmailField(null=False, blank=False)
    c_content = models.TextField(max_length=400, null=False, blank=False)