from statistics import mode
from django.db import models

class links(models.Model):
    ""
    url = models.URLField()
    description = models.TextField(blank=True)
    rating = models.SmallIntegerField(default=1)


