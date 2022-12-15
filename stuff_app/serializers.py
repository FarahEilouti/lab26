from rest_framework import serializers

from .models import Stuff, Post

class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stuff
        # fields=['id','name', 'owner', 'description']
        fields='__all__'


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model= Post 
        fields='__all__'