from rest_framework import generics

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer, UserRegisterSerializer


class UserCreateAPIView(generics. CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]



