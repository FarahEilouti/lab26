from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import StuffSerializer, PostSerializers

from .models import Stuff,Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny,IsAuthenticated

class StuffListView(ListCreateAPIView):
    queryset=Stuff.objects.all()
    serializer_class= StuffSerializer
    #permission_classes=[IsOwnerOrReadOnly]



class StuffDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Stuff.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[IsOwnerOrReadOnly]


class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[AllowAny]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= StuffSerializer
    permission_classes=[IsAuthenticated]