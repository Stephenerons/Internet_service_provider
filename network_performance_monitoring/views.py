from django.shortcuts import render
from rest_framework.views import APIView
from .models import Network_performance
from rest_framework.response import Response
from rest_framework import status
from .serializer import NetworkSerializers
from rest_framework.generics import ListAPIView, RetrieveAPIView


# Create your views here.


class PerformanceListView(ListAPIView):
    queryset = Network_performance.objects.all()
    serializer_class = NetworkSerializers

# Detail view for a specific plan
class PerformanceDetailView(RetrieveAPIView):
    queryset = Network_performance.objects.all()
    serializer_class = NetworkSerializers
    lookup_field = 'id'

    
class PerformanceView(APIView):

    def post(self, request):
        incoming_data =request.data
        serializer = NetworkSerializers(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "customer post request successful"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):
        try:
            bills = Network_performance.objects.get(pk=id)
        except Network_performance.DoesNotExist:
            return Response({"message": "Data not found."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NetworkSerializers(bills, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bills put request successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            bills = Network_performance.objects.get(pk=id)
        except Network_performance.DoesNotExist:
             return Response({"message": "Data not found."}, status=status.HTTP_400_BAD_REQUEST)
        
        bills.delete()
        return Response({"message": "bills delete request successful"}, status=status.HTTP_400_BAD_REQUEST)
    
