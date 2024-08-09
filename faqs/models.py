from django.db import models
from django.utils import timezone

class Faqs(models.Model):
    FAQ_TYPE_CHOICES = [
        ('company', 'Company'),
        ('destination', 'Destination')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    faq_type = models.CharField(max_length=11, choices=FAQ_TYPE_CHOICES, default='company')
    destination = models.ForeignKey(
        'holiday.Destination',
        related_name="faqs_for_destination",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)  # Provide a default value
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
