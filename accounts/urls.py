from django.urls import path
from . import views

urlpatterns = [
    path('seo-get',views.seo,name="seo"),
    path('register-user',views.registeruser,name="registeruser"),
    path('login-user',views.loginuser,name="loginuser"),
    path('profile/',views.profileview,name="profileveiw"),
    path('update-profile',views.updateprofile,name="updateprofile"),
    path('logout',views.log_out,name="logout"),
    path('settings/',views.settings,name="settings"),
    path('delete-account',views.deleteaccount,name="deleteaccount"),
    path('membership',views.membership,name="membership"),
    path('change-password',views.updatepass,name="updatepass"),
    path('activate',views.activate,name="activate"),
    path('reset-password',views.resetpass,name="resetpass"),
    path('google-login',views.googlelogin,name="googlelogin"),
    path('apply-refer',views.applyrefer,name="applyrefer"),
    path('refer-and-earn',views.referearn,name="referearn"),
]
