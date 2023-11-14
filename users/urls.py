from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-retrieve'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
