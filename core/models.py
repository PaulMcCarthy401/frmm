from django.db import models


class Ticket(models.Model):
    # id
    # name
    # phone number
    # location
    # status
    subject = models.TextField()

    def __str__(self):
        return self.subject