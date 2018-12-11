from django.contrib import admin
from django import forms
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget


from .models import Ticket, Mission, Resource



class TicketAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

class MissionAdmin(admin.ModelAdmin):
    # resources_used = forms.ModelChoiceField(queryset=Resource.objects.filter(allocated_to=None))
    class Meta:
        model = Mission

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Resource)