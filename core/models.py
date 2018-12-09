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