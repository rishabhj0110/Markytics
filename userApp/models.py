from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.

class ReportForm(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    LOCATION_CHOICE = (
        ('CH', 'Corporate Headoffice'), 
        ('OD', 'Operations Department'), 
        ('WS', 'Work Station'), 
        ('MD', 'Marketing Division'))
    location = models.CharField(max_length=2, choices=LOCATION_CHOICE)
    location_description = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    SEVERITY_CHOICE = (
        (1, 'Mild'),
        (2, 'Moderate'),
        (3, 'Severe')
    )
    severity = models.IntegerField(choices=SEVERITY_CHOICE, default=0)
    cause = models.CharField(max_length=50, blank=True, null=True)
    actions = models.CharField(max_length=50, blank=True, null=True)
    SUB_INCIDENT_CHOICES = (
        (1, 'Environmental incident'),
        (2, 'Injury/Illness'),
        (3, 'Property Damage'),
        (4, 'Vehicle')
    )
    # include multiselectfield in installed apps in settings.py
    subIncidents = MultiSelectField(choices=SUB_INCIDENT_CHOICES)
    reported_by = models.CharField(max_length=100)

    def __str__(self):
        return self(self.user)

