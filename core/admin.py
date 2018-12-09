from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from .models import Ticket



class TicketAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Ticket, TicketAdmin)
