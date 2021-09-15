from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('seo-get',views.seo,name="seo"),
    path('register-user',views.registeruser,name="registeruser"),
    path('login-user',views.loginuser,name="loginuser"),
    path('profile',views.profileview,name="profileveiw"),
    path('update-profile',views.updateprofile,name="updateprofile"),
    path('logout',views.log_out,name="logout"),
    path('settings',views.settings,name="settings"),
    path('delete-account',views.deleteaccount,name="deleteaccount"),
    path('membership',views.membership,name="membership"),
]