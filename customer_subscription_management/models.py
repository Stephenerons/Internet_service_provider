from django.conf import settings
from django.db import models
from internet_service_plan_management.models import ServicePlanManagement
from django.utils import timezone


# Create your models here.

class SubscriptionManagement(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    service_plan = models.ForeignKey(ServicePlanManagement, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    renewal_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.user} - {self.service_plan.plan_name} ({self.status})"

    class Meta:
        verbose_name = "Customer Subscription"
        verbose_name_plural = "Customer Subscriptions"

    

