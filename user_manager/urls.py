from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('user/register/',UserRegistrationViewSet.as_view(),name='Registration'),
    path('user/reset/password/',ResetPasswordViewSet.as_view(),name='Password reset'),
    path('user/login/',LogInViewSet.as_view(),name='LOGIN'),
    path('user/logout/',LogOutViewSet.as_view(),name='LOGOUT'),
    path('user/request/otp/',RequestOTPViewSet.as_view(),name='Get OTP'),
    path('user/verify/otp/',VerifyOTPViewSet.as_view(),name='Verify OTP')
]