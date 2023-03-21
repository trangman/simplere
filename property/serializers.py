from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'reference', 'title', 'description', 'image', 'bedrooms', 'bathrooms', 'price')
