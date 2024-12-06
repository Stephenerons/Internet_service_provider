from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import BillingManagement, Invoice, Payment
from .serializers import BillingSerializer, InvoiceSerializer, PaymentSerializer
import paypalrestsdk

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE, 
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET
})

class BillListView(ListAPIView):
    queryset = BillingManagement.objects.all()
    serializer_class = BillingSerializer

class BillDetailView(RetrieveAPIView):
    queryset = BillingManagement.objects.all()
    serializer_class = BillingSerializer
    lookup_field = 'id'


class BillingView(APIView):
    def post(self, request):
        serializer = BillingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bill request created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            bill = BillingManagement.objects.get(pk=id)
        except BillingManagement.DoesNotExist:
            return Response({"message": "Data not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BillingSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bill updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            bill = BillingManagement.objects.get(pk=id)
            bill.delete()
            return Response({"message": "Bill deleted successfully"}, status=status.HTTP_200_OK)
        except BillingManagement.DoesNotExist:
            return Response({"message": "Data not found."}, status=status.HTTP_404_NOT_FOUND)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        invoice_id = request.data.get('invoice_id')
        try:
            invoice = Invoice.objects.get(id=invoice_id)
            if invoice.is_paid:
                return Response({'error': 'Invoice already paid'}, status=status.HTTP_400_BAD_REQUEST)
            payment = Payment.objects.create(invoice=invoice, amount=invoice.amount_due)
            invoice.is_paid = True
            invoice.save()
            return Response({'status': 'Payment successful'}, status=status.HTTP_201_CREATED)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)


class PayPalPaymentView(APIView):
    def post(self, request):
        invoice_id = request.data.get('invoice_id')
        try:
            invoice = Invoice.objects.get(id=invoice_id)
            amount = str(invoice.amount_due)  # Ensure amount is formatted correctly
            
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "redirect_urls": {
                    "return_url": request.build_absolute_uri("/payment/execute"),
                    "cancel_url": request.build_absolute_uri("/payment/cancel")
                },
                "transactions": [{
                    "amount": {"total": amount, "currency": "USD"},
                    "description": f"Payment for Invoice ID {invoice_id}",
                    "custom": str(invoice_id)  # Store invoice ID in transaction for retrieval
                }]
            })

            if payment.create():
                for link in payment.links:
                    if link.rel == "approval_url":
                        return Response({"approval_url": link.href}, status=status.HTTP_200_OK)
                return Response({"error": "Approval URL not found"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Payment creation failed", "details": payment.error}, status=status.HTTP_400_BAD_REQUEST)
        
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)



class PayPalExecuteView(APIView):
    def get(self, request):
        payment_id = request.GET.get('paymentId')
        payer_id = request.GET.get('PayerID')
        
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            # Retrieve invoice_id from custom field
            invoice_id = payment.transactions[0].custom  
            try:
                invoice = Invoice.objects.get(id=invoice_id)
                invoice.is_paid = True
                invoice.save()
                return Response({"status": "Payment executed successfully"}, status=status.HTTP_200_OK)
            except Invoice.DoesNotExist:
                return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Payment execution failed", "details": payment.error}, status=status.HTTP_400_BAD_REQUEST)

