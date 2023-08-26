from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Group(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
    
    def __str__(self) -> str:
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='BlogApp', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    group = models.ManyToManyField(Group)
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
    
    def __str__(self) -> str:
        return self.title    