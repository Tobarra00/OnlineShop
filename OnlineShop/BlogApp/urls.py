from django.urls import path
from BlogApp import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('groups/<int:group_id>/', views.groups, name="groups")
]

