from django.conf import settings
from django.urls import reverse


def djangoSettings(request):
    user = request.user
    return {"djangoSettings": settings, "user":user}
