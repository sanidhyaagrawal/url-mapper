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


    
def url_redirect(request, sub_url):
    try:
        site_obj = sites.objects.get(sub_url=sub_url)
    except sites.DoesNotExist:
        try:
            site_obj = sites.objects.get(sub_url="404")
            return redirect(site_obj.target_url)
        except sites.DoesNotExist:
            return render(request, '404.html')
    return redirect(site_obj.target_url)
    