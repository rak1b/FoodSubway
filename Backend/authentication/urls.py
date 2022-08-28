from django.urls import path
from authentication.views import  LoginView, ProfileView, SignUpView,ForgetPasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('access_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('forget_password/', ForgetPasswordView.as_view(), name='forgetpassword'),

]