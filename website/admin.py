from django.contrib import admin
from django.contrib.admin import ModelAdmin, site
from .models import *


 
class sites_admin(ModelAdmin):
    search_fields = ('sub_url', 'target_url' ,'date')
    list_display = ('sub_url', 'target_url' ,'date')
    list_display_links = ('sub_url', 'target_url' ,'date')
    list_filter =('date',)
    readonly_fields = ('date',)
 

 

class analytics_admin(ModelAdmin):
    search_fields = ('source' ,'device')
    list_display = ('site', 'source' ,'device', 'ip_location', 'ip', 'date')
    list_display_links = ('site', 'source' ,'device', 'ip', 'date')
    list_filter = ('site', 'source' ,'device', 'ip', 'date')

    readonly_fields = ('date', 'ip_location')
 


site.register(sites, sites_admin)

site.register(analytics, analytics_admin)
