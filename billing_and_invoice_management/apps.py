from django.apps import AppConfig

class BillingAndInvoiceManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing_and_invoice_management'

    def ready(self):
        import billing_and_invoice_management.signals
