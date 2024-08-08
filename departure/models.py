# Create your models here.
from django.db import models

class Departure(models.Model):
    upcoming_departure_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    upcoming_departure_status = models.BooleanField(default=False, null=True, blank=True)
    upcoming_departure_price = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"Departure on {self.upcoming_departure_date} - Status: {'Active' if self.upcoming_departure_status else 'Inactive'} - Price: {self.upcoming_departure_price}"
