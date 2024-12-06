from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import ServicePlanManagement

from .serializer import ServiceSerializers
from rest_framework import status


# Create your views here.


class PlanListView(ListAPIView):
    queryset = ServicePlanManagement.objects.all()
    serializer_class = ServiceSerializers

# Detail view for a specific plan
class PlanDetailView(RetrieveAPIView):
    queryset = ServicePlanManagement.objects.all()
    serializer_class = ServiceSerializers
    lookup_field = 'id'

class PlanViews(APIView):
    
    def post(self, request):
        incoming_data =request.data
        serializer = ServiceSerializers(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "plans post request successful"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):
        try:
            plans = ServicePlanManagement.objects.get(pk=id)

        except ServicePlanManagement.DoesNotExist:
             return Response({"message": "Data not found."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ServiceSerializers(plans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Plans put request successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Plans put request unsuccessful"}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        try:
            plans = ServicePlanManagement.objects.get(pk=id)
        except ServicePlanManagement.DoesNotExist:
             return Response({"message": "Data not found."}, status=status.HTTP_400_BAD_REQUEST)
        
        plans.delete()
        return Response({"message": "Plans delete request successful"}, status=status.HTTP_400_BAD_REQUEST)
    


