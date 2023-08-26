from django.contrib import admin
from BlogApp import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Group, GroupAdmin)
