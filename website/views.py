from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout

def index(request):
    if not request.user.is_superuser: 
        return render(request, 'index.html')
    else:
        return redirect("/dev/add")       


def add(request):
    if request.user.is_superuser: 
        return render(request, 'add.html')
    else:
        return render(request, 'login.html')

def view_logout(request):
    logout(request)
    return redirect("/")       


def url_redirect(request, sub_url, tracking_id = None):
    try:
        site_obj = sites.objects.get(sub_url=sub_url)
        try:
            device= request.META.get('HTTP_USER_AGENT').split("(")[1].split(")")[0]    
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        except:
            device = None
            ip = None

        analytics.objects.create(device=device, source=tracking_id, ip=ip, site=site_obj)

    except sites.DoesNotExist:
        try:
            site_obj = sites.objects.get(sub_url="404")
            return redirect(site_obj.target_url)
        except sites.DoesNotExist:
            return render(request, '404.html')
    return redirect(site_obj.target_url)
    