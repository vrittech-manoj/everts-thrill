from django.urls import path
from .views import EmailCheckView, CustomPasswordResetView , VerifyUserPasswordToken,ContactmeView,EmailChangeGetOtpView,EmailResetView,EmailChangeOtpVerifyView


urlpatterns = [
    path('get-otp/', EmailCheckView.as_view()),
    path('get-otp-email-change/', EmailChangeGetOtpView.as_view()),
    path('email-reset/', EmailResetView.as_view(), name="reset-password"),
    path('password-reset/', CustomPasswordResetView.as_view(), name="reset-password"),
    path('email-reset-otp-verify/', EmailChangeOtpVerifyView.as_view(), name="reset-password"),
    path('verify-token/', VerifyUserPasswordToken.as_view(), name="VerifyUserPasswordToken"),

    path('contact-me/',ContactmeView.as_view(),name="ContactmeView"),
]
