from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime
from django.utils.timezone import now
# Create your models here.

class Inquiry(models.Model):
    name = models.CharField( max_length=100)
    zip = models.CharField(max_length=7, blank=True)
    prefecture = models.IntegerField(blank=True,validators=[MinValueValidator(0), MaxValueValidator(50)])
    address1 = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    content = models.TextField(max_length=10000)
    create_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)