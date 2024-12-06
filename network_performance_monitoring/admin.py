from django.contrib import admin

from .models import Network_performance

# Register your models here.
class Network_performance_admin(admin.ModelAdmin):
    list_display= ('user', 'status', 'download_speed', 'upload_speed', 'latency_speed', 'uptime')

admin.site.register(Network_performance ,Network_performance_admin)