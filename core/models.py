from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth import get_user_model


class Ticket(models.Model):
    # id
    # name
    # phone number
    # location
    # status
    subject = models.TextField()
    location = PointField(srid=4326, blank=False, null=True)

    def __str__(self):
        return self.subject

class Mission(models.Model):
    # id
    # priority
    # date created
    # description
    # status => [not started, in progress, finished, failed]
    # related_tickets

    STATUS_TYPES = (
        ('NS', "Not Started"),
        ('IP', "In Progress"),
        ('S', "Finished"),
        ('F', 'Failure')
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    priority = models.IntegerField(blank=False, default=0)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_TYPES)
    related_tickets = models.ManyToManyField(Ticket)
    first_responders = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.description
    
    def get_bootstrap_badge_type(self):
        if self.status == 'NS':
            return 'secondary'
        elif self.status == 'IP':
            return 'primary'
        elif self.status == 'S':
            return 'success'
        elif self.status == 'F':
            return 'danger'

class Resource(models.Model):
    name = models.TextField(max_length=120)
    allocated_to = models.ForeignKey(Mission, on_delete=models.SET_NULL, blank=True, null=True)