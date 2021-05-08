from django.urls import path
from . import views, apis

urlpatterns = [
    path('', views.index, name='index'), 
    path('dev/add', views.add, name='index'), 
    path('dev/logout', views.view_logout, name='view_logout'), 
    path('api/short/', apis.shorten_api, name='shorten_api'), 
    path('api/login/', apis.login_api, name='login_api'), 

    path('<str:sub_url>', views.url_redirect, name='url_redirect'), 

]

