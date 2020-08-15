from django.shortcuts import render
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from post.serializers import UserSerializer
from rest_framework import permissions
from rest_framework import generics
from post.permissions import IsOwnerOrReadonly


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
  
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]


