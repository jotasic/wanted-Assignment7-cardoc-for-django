from rest_framework import serializers

from .models        import Tire


class TireSerializers(serializers.ModelSerializer):
    width       = serializers.CharField()
    wheelSize   = serializers.CharField(source='wheel_size')
    aspectRatio = serializers.CharField(source='aspect_ratio')

    class Meta:
        model  = Tire
        fields = ('width', 'wheelSize', 'aspectRatio')