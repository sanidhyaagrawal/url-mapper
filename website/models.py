from django.db import models

# Create your models here.

class sites(models.Model):
    sub_url = models.CharField(max_length=100)
    target_url = models.URLField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
