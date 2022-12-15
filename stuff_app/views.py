from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import StuffSerializer, PostSerializers

from .models import Stuff,Post
from .permissions import IsOwnerOrReadOnly

class StuffListView(ListCreateAPIView):
    queryset=Stuff.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[IsOwnerOrReadOnly]



class StuffDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Stuff.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[IsOwnerOrReadOnly]


class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]