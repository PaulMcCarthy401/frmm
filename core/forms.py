import sys
from django import forms
from core.models import Ticket

from mapwidgets.widgets import GooglePointFieldWidget


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'location']

        widgets = {
            'location': GooglePointFieldWidget,
        }

    def form_valid(self, form):
        # self.object = form.save()

        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print(sys.stderr, "Form was invalid")
        return HttpResponseRedirect(self.get_success_url())