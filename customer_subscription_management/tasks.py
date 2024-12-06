from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from billing_and_invoice_management.models import Invoice
from customer_subscription_management.models import SubscriptionManagement

@shared_task
def generate_invoices():
    today = timezone.now()
    active_subscriptions = SubscriptionManagement.objects.filter(renewal_date__gte=today)


    for subscription in active_subscriptions:
        Invoice.objects.create(
            user = subscription.user,
            service_plan=subscription.service_plan,
            amount=subscription.service_plan.price,
            date_generated =today,
            due_date = today + timezone.timedelta(days=30),
        )
        subscription.renewal_date = today + timedelta(days=30)
        subscription.save()
