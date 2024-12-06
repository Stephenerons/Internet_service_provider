from django.conf import settings
from django.db import models
from customer_subscription_management.models import SubscriptionManagement

# Create your models here.
class BillingManagement(models.Model):

    BILLING_PERIOD_CHOICES =[
        ('monthly', 'Monthly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('yearly', 'Yearly')

    ] 

    PAYMENT_STATUS_CHOICES =[
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('due', 'Due')

    ] 

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubscriptionManagement, on_delete=models.CASCADE, null=True, blank=True)
    billing_period = models.CharField(max_length=200, choices=BILLING_PERIOD_CHOICES)
    due_date = models.DateField()


    def get_amount(self):
        return self.subscription.service_plan.price if self.subscription else 0.00
    
    def get_payment_status(self):
        last_invoice = self.subscription.invoices.order_by('-due_date').first()
        return "paid" if last_invoice and last_invoice.is_paid else "due"


    def __str__(self):
        return f"Billing for {self.subscription} - Status: {self.get_payment_status()}"
    


class Invoice(models.Model):
    subscription = models.ForeignKey(SubscriptionManagement, on_delete=models.CASCADE, related_name='invoices')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    invoice_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.subscription.user} - Due: {self.due_date}"

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"



class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits= 10, decimal_places = 2)
    date_paid = models.DateField(auto_now_add=True)
    
