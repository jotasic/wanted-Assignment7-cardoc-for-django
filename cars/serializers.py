from rest_framework import serializers

from .models        import Tire


class TireSerializers(serializers.ModelSerializer):
    width       = serializers.IntegerField()
    wheelSize   = serializers.IntegerField(source='wheel_size')
    aspectRatio = serializers.IntegerField(source='aspect_ratio')

    class Meta:
        model  = Tire
        fields = ('width', 'wheelSize', 'aspectRatio')