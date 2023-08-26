from django.shortcuts import render
from BlogApp import models

# Create your views here.


def blog(request):
    
    blogs = models.Blog.objects.all()
    
    
    return render(request, 'BlogApp/blog.html', {'blogs': blogs})

def groups(request, group_id):
    
    groups = models.Group.objects.get(id=group_id)
    
    blogs = models.Blog.objects.filter(group=groups)
    
    return render(request, 'BlogApp/blog.html', {'groups': groups, 'blogs': blogs})