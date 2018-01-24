from django.db import models

# Create your models here.

class Average(models.Model):
    """
    Models for representing Average object
    """
    #Average value
    value = models.FloatField(null=True, blank=True)

    #Timestamp
    created = models.DateTimeField(auto_now_add=True)

