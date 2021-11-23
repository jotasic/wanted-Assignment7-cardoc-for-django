from importlib.util import source_from_cache
from django.contrib.auth        import get_user_model
from rest_framework import serializers


class SingupSerializers(serializers.ModelSerializer):
    class Meta:
        model        = get_user_model()
        fields       = ('user_id', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class UserTireRegisterSerializer(serializers.Serializer):
    id     = serializers.CharField()
    trimId = serializers.IntegerField()