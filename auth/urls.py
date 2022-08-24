from django.urls import path
from auth.views import  ChangePasswordView, LoginView, ProfileView, SignUpView, PasswordResetView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='changepassword'),
    path('reset-password/<uid>/<token>/', PasswordResetView.as_view(), name='reset-password'),

]