from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import status


from django.contrib.auth.models import auth
from django.utils import timezone
from .models import *
from .responces import getResponce
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

#In some cases end user might want to go back to add/remove some files and then again 
#return to the next screen which is not possible with csrf velidation
#we have to exempt csrf validation for these perticular apis in order to achive this functionality.
#This is achived using this-
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening



@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication, SessionAuthentication, BasicAuthentication])
def shorten_api(request):
    if request.user.is_superuser:
        data = request.data
        base =data['base'].strip()
        target =data['target'].strip()
        
        if len(base) == 0:
            return Response({'error': "sub-url is required"}, status=status.HTTP_200_OK)

        print(base, target)

        validate = URLValidator()
        try:
            validate(target)
        except ValidationError as e:
            print(e)
            return Response({'error': "invalid target URL"}, status=status.HTTP_200_OK)


        sites.objects.create(sub_url=base, target_url=target)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


@api_view(['POST'])
@throttle_classes([AnonRateThrottle]) 
@authentication_classes([SessionAuthentication])
def login_api(request):
    data = request.data
    username =data['username'].strip()
    password =data['password'].strip()
    
    if len(username) == 0:
        return Response({'error': "username is required"}, status=status.HTTP_200_OK)

    
    if len(password) == 0:
        return Response({'error': "password is required"}, status=status.HTTP_200_OK)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_superuser:
            login(request, user)
            return Response(status=status.HTTP_202_ACCEPTED)

    return Response({'error': "Invalid credentials"}, status=status.HTTP_200_OK)




