from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='5/m', block=True)  # anonymous users
def anonymous_sensitive_view(request):
    return JsonResponse({"message": "Anonymous access allowed"})


@login_required
@ratelimit(key='ip', rate='10/m', block=True)  # authenticated users
def authenticated_sensitive_view(request):
    return JsonResponse({"message": "Authenticated access allowed"})
