from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import django_filters
import rest_framework
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly

# Create your views here.


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        rest_framework.filters.OrderingFilter,
    ]
    filterset_fields = ["title"]
    ordering_fields = ["title"]
    permission_classes = [IsAuthorOrReadOnly]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
