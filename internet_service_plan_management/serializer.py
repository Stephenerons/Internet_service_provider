from rest_framework import serializers
from .models import ServicePlanManagement

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicePlanManagement
        fields= '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def create(self, validated_data):
        return ServicePlanManagement.objects.create(**validated_data)
    

    def update(self,  instance, validated_data):
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.speed = validated_data.get('speed', instance.speed)
        instance.data_limit = validated_data.get('data_limit', instance.data_limit)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    

