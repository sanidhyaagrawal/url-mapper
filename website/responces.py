from rest_framework.response import Response
from rest_framework import status


#centralized responces for all the APIs for this app (users)
#is used for internationalization of responses
def getResponce(*args):
    responces = {
        "login_invalid_credentials" : Response({'error': "Invalid credentials, try again"}, status=status.HTTP_200_OK),
        "signup_no_firstname" : Response({'error': "Name is reqired"}, status=status.HTTP_200_OK),
        "invalid_phone_number" : Response({'error': "Invalid Phone Number"}, status=status.HTTP_200_OK),
        "invalid_email" : Response({'error': "No account associated with this email."}, status=status.HTTP_200_OK),
        "pick_year" : Response({'error': "Select Year of Birth"}, status=status.HTTP_200_OK),
        "invalid_year" : Response({'error': "Invalid Year."}, status=status.HTTP_200_OK),
        "upload_image" : Response({'error': "Upload an image"}, status=status.HTTP_200_OK),
        "phone_number_used" : Response({'error': "Phone number alredy used"}, status=status.HTTP_200_OK),

    }
    return responces[args[0]]
   