from django.urls import path
from . import views

urlpatterns = [
    path('privacy-policy',views.privacypolicy,name="privacypolicy"),
]
