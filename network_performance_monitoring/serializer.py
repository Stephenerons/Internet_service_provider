from rest_framework import serializers
from .models import Network_performance


class NetworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Network_performance
        fields = '__all__'

    def create(self, validated_data):
        return Network_performance.objects.create(**validated_data)

    def update(self,  instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.download_speed = validated_data.get(
            'download_speed', instance.download_speed)
        instance.upload_speed = validated_data.get(
            'upload_speed', instance.upload_speed)
        instance.latency_speed = validated_data.get(
            'latency_speed', instance.latency_speed)
        instance.uptime = validated_data.get('uptime', instance.uptime)
        instance.save()
        return instance
