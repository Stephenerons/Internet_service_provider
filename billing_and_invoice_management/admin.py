from django.contrib import admin
from .models import BillingManagement, Invoice, Payment

class BillingAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'billing_period', 'payment_status_display', 'amount_display', 'due_date')

    def amount_display(self, obj):
        return obj.get_amount()
    amount_display.short_description = 'Amount'

    def payment_status_display(self, obj):
        return obj.get_payment_status()
    payment_status_display.short_description = 'Payment Status'

admin.site.register(BillingManagement, BillingAdmin)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'amount_due', 'due_date', 'is_paid', 'invoice_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'date_paid')
