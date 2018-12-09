from django.db import models
from django.contrib.gis.db.models import PointField


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

    priority = models.IntegerField(blank=False, default=0, min_value=0, max_value=10)
    date_created = models.DateTimeField()
    description = models.TextField()
    status = models.ChoiceField(choices=STATUS_TYPES)

    def __str__(self):
        return self.subject