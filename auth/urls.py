from django.urls import path
from auth.views import  LoginView, ProfileView, SignUpView,ForgetPasswordView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('forget_password/', ForgetPasswordView.as_view(), name='forgetpassword'),

]