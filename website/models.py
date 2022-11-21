from django.db import models
import re
import json
import requests
# Create your models here.

class sites(models.Model):
    sub_url = models.CharField(max_length=100, unique=True)
    target_url = models.URLField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.sub_url)

class analytics(models.Model):
    device = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=10, null=True)
    ip = models.URLField(max_length=100, null=True)
    site = models.ForeignKey(sites, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    
    def ip_location(self):
        import requests
        try:
            ip = self.ip.split(", ")[0]
            response = requests.get("https://geolocation-db.com/json/{}&position=true".format( ip ) ).json()
            print(response)
            location = ""
            city = response["city"]
            state = response["state"]
            country_name = response["country_name"]

            if city:
                location += city + ", "

            if state:
                location += state + ", "

            if country_name:
                location += country_name


            return location
        except:
            return "-"