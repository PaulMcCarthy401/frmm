from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, FormView, UpdateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from django.utils import timezone
from django.views.generic.list import ListView

import sys
from .models import Ticket, Mission
from .forms import TicketForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.auth import get_user_model


#https://stackoverflow.com/questions/4789021/in-django-how-do-i-check-if-a-user-is-in-a-certain-group
#https://bradmontgomery.net/blog/restricting-access-by-group-in-django/

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'ticket_list'

    def get_queryset(self):
        """Return all tickets."""
        return Ticket.objects.all()

# class TicketCreate(FormView):
#     template_name = 'core/index.html'
#     success_url = './'
        
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         form.helper = FormHelper()
#         form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary'))
#         return form

class TicketCreate(CreateView):
    model = Ticket
    template_name = 'core/index.html'
    success_url = './'
    form_class = TicketForm
        
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary'))
        return form

class VolunteerPage(CreateView):
    model = Ticket
    template_name = 'core/volunteer.html'
    success_url = './'

class FirstResponderPage(CreateView):
    model = Ticket
    template_name = 'core/first_responder.html'
    success_url = './'

class FirstResponderChiefPage(ListView):
    model = Mission
    paginate_by = 100  # if pagination is desired
    template_name = 'core/first_responder_chief.html'
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

class MissionCreate(CreateView):
    model = Mission
    fields = '__all__'
    success_url = '/firstresponderchief'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary float-right'))

        form.fields['first_responders'].queryset = get_user_model().objects.filter(groups__name='First Responder')

        return form

class MissionUpdate(UpdateView):
    model = Mission
    fields = '__all__'
    success_url = '/firstresponderchief'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Update', css_class='btn-primary float-right'))

        form.fields['first_responders'].queryset = get_user_model().objects.filter(groups__name='First Responder')

        return form

# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
# -> UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Add the user to the Volunteers group
            volunteer_group = Group.objects.get(name='Volunteer') 
            volunteer_group.user_set.add(user)

            login(request, user)
            return redirect('core:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})