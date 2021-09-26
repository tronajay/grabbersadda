from django.contrib import admin
from .models import Page, Giveaway, GiveawayParticipants
# Register your models here.
admin.site.register(Page)
admin.site.register(Giveaway)
admin.site.register(GiveawayParticipants)