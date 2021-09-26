from django.urls import path
from . import views

urlpatterns = [
    path('page/<str:slug>',views.pagecontent,name="pagecontent"),
    path('giveaway',views.giveaway,name="giveaway"),
    path('add-participant',views.addparticipant,name="addparticipant"),
]
