from django.contrib import admin
from .models import RequestLog, BlockedIP, SuspiciousIP

# Task 0: RequestLog
@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'path', 'timestamp', 'country', 'city')
    list_filter = ('timestamp', 'country', 'city')
    search_fields = ('ip_address', 'path', 'country', 'city')
    readonly_fields = ('ip_address', 'path', 'timestamp', 'country', 'city')

# Task 1: BlockedIP
@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)
    search_fields = ('ip_address',)

# Task 4: SuspiciousIP
@admin.register(SuspiciousIP)
class SuspiciousIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'reason', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('ip_address', 'reason')
    readonly_fields = ('ip_address', 'reason', 'timestamp')
