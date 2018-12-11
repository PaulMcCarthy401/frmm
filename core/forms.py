import sys
from django import forms
from django.contrib.gis.forms import PointField
from core.models import Ticket, Mission, Resource

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'location']

        widgets = {
            'location': GooglePointFieldWidget,
        }

    # def form_valid(self, form):
    #     # self.object = form.save()

    #     # do something with self.object
    #     # remember the import: from django.http import HttpResponseRedirect
    #     return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form):
    #     print(sys.stderr, "Form was invalid")
    #     return HttpResponseRedirect(self.get_success_url())

class TicketReadonlyForm(forms.Form):
    subject = forms.CharField()
    location = PointField(widget=GoogleStaticOverlayMapWidget)


# class MissionForm(forms.ModelForm):
#     class Meta:
#         model = Mission
#         fields = '__all__'

#     def form_valid(self, form):
#         # self.object = form.save()

#         # do something with self.object
#         # remember the import: from django.http import HttpResponseRedirect
#         return HttpResponseRedirect(self.get_success_url())

#     def form_invalid(self, form):
#         print(sys.stderr, "Form was invalid")
#         return HttpResponseRedirect(self.get_success_url())