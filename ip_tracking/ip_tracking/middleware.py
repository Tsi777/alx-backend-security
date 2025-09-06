from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from ip_tracking.models import RequestLog, BlockedIP
from ipware import get_client_ip
from django.core.cache import cache
import requests

IPGEO_API_KEY = 'YOUR_API_KEY'

class IPTrackingMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        ip, is_routable = get_client_ip(request)
        if not ip:
            ip = '0.0.0.0'

        # Superuser bypass
        if request.user.is_authenticated and request.user.is_superuser:
            pass  # never block superuser

        else:
            if BlockedIP.objects.filter(ip_address=ip).exists():
                return HttpResponseForbidden("Your IP is blocked.")

        # Geolocation caching
        cache_key = f"geo_{ip}"
        geo_data = cache.get(cache_key)
        if not geo_data:
            try:
                response = requests.get(
                    f"https://api.ipgeolocation.io/ipgeo?apiKey={IPGEO_API_KEY}&ip={ip}"
                )
                data = response.json()
                geo_data = {
                    "country": data.get("country_name", ""),
                    "city": data.get("city", "")
                }
                cache.set(cache_key, geo_data, 60*60*24)
            except:
                geo_data = {"country": "", "city": ""}

        # Log request
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            country=geo_data["country"],
            city=geo_data["city"]
        )
