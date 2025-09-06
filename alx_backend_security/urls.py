from django.urls import path
from ip_tracking.admin_dashboard import security_admin

urlpatterns = [
    path('admin/', security_admin.urls),
]
