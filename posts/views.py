from django.shortcuts import render
from .models import Post
from rest_framework import generics
from serializers import PostSerializer


# Create your views here.

class PostList(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
