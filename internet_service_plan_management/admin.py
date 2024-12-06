from django.contrib import admin

from .models import ServicePlanManagement

# Register your models here.
class Plan_management_admin(admin.ModelAdmin):
    list_display= ('plan_name', 'speed', 'data_limit', 'price', 'description' )
    search_fields = ('plan_name', 'speed', 'price')


admin.site.register(ServicePlanManagement ,Plan_management_admin)