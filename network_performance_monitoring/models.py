from django.db import models
from django.conf import settings

# Create your models here.
class Network_performance(models.Model):

    STATUS_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('bad', 'Bad'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='good')
    download_speed =models.FloatField(help_text="Download speed in Mbps")
    upload_speed = models.FloatField(help_text="upload speed in Mbps")
    latency_speed = models.FloatField(help_text="Latency speed in milliseconds")
    uptime =models.FloatField(help_text="Uptime percentage (0-100%)")

    def __str__(self):
        return f"Network Performance for {self.user} at {self.timestamp}"

    class Meta:
        verbose_name = "Network Performance"
        verbose_name_plural = "Network Performances"