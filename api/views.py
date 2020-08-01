from rest_framework import generics, permissions
from recipes.models import Recipe
from users.models import User
from .serializers import RecipeSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, IsSuperUser


class RecipeAPIView(generics.ListAPIView):
    # Permissions:
    #     Authenticated: R
    #     Superuser: RW
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Permissions:
    #   Authenticated: R
    #   Superuser: RW
    #   Recipe author: RW
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserAPIView(generics.ListAPIView):
    # Permissions:
    #     Superuser: RW
    permission_classes = (IsSuperUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
