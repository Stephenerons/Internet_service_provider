from rest_framework import serializers
from .models import BillingManagement, Invoice, Payment


class BillingSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(source='get_amount', max_digits=10, decimal_places=2, read_only=True)
    payment_status = serializers.CharField(source='get_payment_status', read_only=True)

    class Meta:
        model = BillingManagement
        fields = ['id', 'user', 'subscription', 'billing_period', 'due_date', 'amount', 'payment_status']


class InvoiceSerializer(serializers.ModelSerializer):
    subscription_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'subscription_id', 'amount_due', 'due_date', 'is_paid', 'invoice_date']


class PaymentSerializer(serializers.ModelSerializer):
    invoice_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'invoice_id', 'amount', 'date_paid']
        read_only_fields = ['date_paid']
