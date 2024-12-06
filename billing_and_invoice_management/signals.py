from django.db.models.signals import post_save
from django.dispatch import receiver

from billing_and_invoice_management.models import BillingManagement, Invoice




@receiver(post_save, sender=BillingManagement)
def create_invoice_for_bill(sender, instance, created, **kwargs):
    if created:
        # Calculate the amount based on the subscription’s service plan price
        amount_due = instance.get_amount()
        # Create an invoice for the newly created bill
        Invoice.objects.create(
            subscription=instance.subscription,
            amount_due=amount_due,
            due_date=instance.due_date
        )

