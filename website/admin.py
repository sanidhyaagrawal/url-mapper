from django.contrib import admin
from django.contrib.admin import ModelAdmin, site
from .models import *


 
class sites_admin(ModelAdmin):
    search_fields = ('sub_url', 'target_url' ,'date')
    list_display = ('sub_url', 'target_url' ,'date')
    list_display_links = ('sub_url', 'target_url' ,'date')
    list_filter =('date',)
    readonly_fields = ('date',)
 



site.register(sites, sites_admin)

