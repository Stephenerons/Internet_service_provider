from django.contrib import admin

from .models import SubscriptionManagement

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display= ( 'user', 'service_plan', 'start_date', 'renewal_date' )

admin.site.register(SubscriptionManagement,CustomerAdmin)