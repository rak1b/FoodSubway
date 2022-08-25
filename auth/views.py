from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from auth.serializers import ForgetPasswordSerializer, LoginSerializer, ProfileSerializer, SignUpSerializer
from django.contrib.auth import authenticate
# from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly
from core.models import User
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
  def patch(self, request, format=None): 
    user = request.user
    profile = User.objects.get(id=user.id)
    serializer = ProfileSerializer(instance=profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ForgetPasswordView(APIView):
  permission_classes = [AllowAny,]
  def post(self, request, format=None):
      serializer = ForgetPasswordSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)


