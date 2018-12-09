from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Ticket
from .forms import TicketForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#https://stackoverflow.com/questions/4789021/in-django-how-do-i-check-if-a-user-is-in-a-certain-group
#https://bradmontgomery.net/blog/restricting-access-by-group-in-django/

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'ticket_list'

    def get_queryset(self):
        """Return all tickets."""
        return Ticket.objects.all()

class TicketCreate(CreateView):
    model = Ticket
    fields = ['subject']
    template_name = 'core/index.html'
    success_url = './'
        
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary'))
        return form