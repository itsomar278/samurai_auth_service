from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]