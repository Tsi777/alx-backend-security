from django.db import models

# Task 0: Request logging
class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, blank=True, null=True)  # Task 2
    city = models.CharField(max_length=100, blank=True, null=True)     # Task 2

    def __str__(self):
        return f"{self.ip_address} - {self.path} - {self.timestamp}"

# Task 1: IP Blacklisting
class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.ip_address

# Task 4: Suspicious IPs
class SuspiciousIP(models.Model):
    ip_address = models.GenericIPAddressField()
    reason = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.reason}"
