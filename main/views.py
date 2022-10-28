
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import AccountSerializer

from .models import Account
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
# Create your views here.



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        
        token['username'] = user.username
        token['email'] = user.email
       
        token['is_superuser'] = user.is_superuser
        token['mobile'] = user.mobile
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterAccount(APIView):

    serializer_class =AccountSerializer

    

    def post(self,request,format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)       


