from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import SubscriptionManagement
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import CustomerSerializer


# Create your views here.

class SubscriptionListView(ListAPIView):
    queryset = SubscriptionManagement.objects.all()
    serializer_class = CustomerSerializer


class SubscriptionDetailView(RetrieveAPIView):
    queryset = SubscriptionManagement.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'


class CustomerView(APIView):

    def post(self, request):
        incoming_data =request.data
        serializer = CustomerSerializer(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "customer post request successful"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):

        subscription = get_object_or_404(SubscriptionManagement, pk=id)

        serializer = CustomerSerializer(subscription, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer put request successful"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    def delete(self, request, id):
        try:
            customer = SubscriptionManagement.objects.get(pk=id)
        except SubscriptionManagement.DoesNotExist:
            return Response({"message": "Data not found."}, status=status.HTTP_404_NOT_FOUND)
        
        customer.delete()
        return Response({"message": "Customer delete request successful"}, status=status.HTTP_200_OK)