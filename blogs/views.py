from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import django_filters
import rest_framework
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

from rest_framework import viewsets

# Create your views here.


# class PostList(generics.ListCreateAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [
#         django_filters.rest_framework.DjangoFilterBackend,
#         rest_framework.filters.OrderingFilter,
#     ]
#     filterset_fields = ["title"]
#     ordering_fields = ["title"]
#     permission_classes = [IsAuthorOrReadOnly]


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthorOrReadOnly]


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        rest_framework.filters.OrderingFilter,
    ]
    filterset_fields = ["title"]
    ordering_fields = ["title"]
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
