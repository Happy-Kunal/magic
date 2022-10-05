import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class ShortURL(models.Model):
    original_url = models.CharField(max_length=2000, null=False)
    shorten_url = models.CharField(max_length=7, null=False)
    created_on = models.DateField(default=datetime.date.today)
    last_used_on = models.DateField(default=datetime.date.today)
    total_hits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.shorten_url} => hits: {self.total_hits}, created_on: {self.created_on}"
    
    def is_older_than_4_years(self):
        return (datetime.date().today() - self.created_on) > datetime.timedelta(year=4)
    

    