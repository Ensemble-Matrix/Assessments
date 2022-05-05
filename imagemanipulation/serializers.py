from rest_framework import serializers
from imagemanipulation.models import Imager

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imager
        fields = ['actual_label', 'image'] 
