from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from auth.serializers import ChangePasswordSerializer, LoginSerializer, PasswordResetSerializer, ProfileSerializer, SignUpSerializer
from django.contrib.auth import authenticate
# from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class SignUpView(APIView):
  def post(self, request, format=None):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
  def post(self, request, format=None):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phone = serializer.data.get('phone')
    password = serializer.data.get('password')
    user = authenticate(phone=phone, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['phone or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class ProfileView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = ChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)



class PasswordResetView(APIView):
  def post(self, request, uid, token, format=None):
    serializer = PasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
  
  
  # https://www.youtube.com/watch?v=lo7lBD9ynVc&ab_channel=GeekyShows