
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/', include('internet_service_plan_management.urls')),
    path('api/', include('customer_subscription_management.urls')),
    path('api/', include('network_performance_monitoring.urls')),
    path('api/', include('billing_and_invoice_management.urls')),
]
