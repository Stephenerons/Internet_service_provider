from rest_framework import serializers
from internet_service_plan_management.serializer import ServiceSerializers
from .models import SubscriptionManagement

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionManagement
        fields = '__all__'


    def create(self, validated_data):
        return SubscriptionManagement.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.renewal_date = validated_data.get('renewal_date', instance.renewal_date)
        instance.service_plan = validated_data.get('service_plan', instance.service_plan)
        instance.save()
        return instance
    
