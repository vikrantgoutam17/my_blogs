from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import reverse
from .views import (
    
    PostUpdateView,
   
   
)
app_name='blogs'
urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('register/',views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("addblog/", views.add_request, name="addblog"),
    path("<user_name>/account/", views.users,name="users"),
    path("<user_name>/profile/", views.user,name="user"),
    path("delete/", views.delete,name="delete"),
    path("accounts/login/",views.login_request, name="login"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('<user_name>/update_details/', views.update, name="update-details"),
    path('<int:pk>/delete/', views.deletes,name="post-delete'"),
    path('<int:pk>/like/', views.like,name="post-like'"),
    path('<int:pk>/likes/', views.likess,name="post-like'"),
    path('<int:pk>/dislike/', views.dislike,name="post-disike'"),
     path('<int:pk>/notify/', views.notify,name="post-disike'"),


    
    ]
