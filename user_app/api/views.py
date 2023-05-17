from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerilaizer
from rest_framework.authtoken.models import Token
from user_app import models 
 

@api_view(['POST',])
def registration_View(request):

    # after registration user have to login first then token will be generated.
    # if request.method == 'POST':
    #     serializer = RegistrationSerilaizer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        
    #     return Response(serializer.errors)
    


    # this is used after registration user will be logged in user token will be generated after registration.
    # after creating this methord have to add some code into models.py file related to token generation form the documentation.
    if request.method == 'POST':
        serializer = RegistrationSerilaizer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'successfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username

            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)




@api_view(['POST',])
def Logout_view(request): 

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

