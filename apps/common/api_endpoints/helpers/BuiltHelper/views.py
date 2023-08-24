from django.core.cache import cache
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.utils import send_telegram_message


class BuiltHelperAPIView(APIView):
    def get(self, request, *args, **kwargs):
        send_telegram_message("Hello from built helper")

        send_telegram_message.delay("Hello from celery built helper")

        cache.set("temp_key", f"Hello from Cache  |  {timezone.localtime()}", 60 * 60 * 24)
        cache_response = cache.get("temp_key")

        send_telegram_message(f"Cache response: {cache_response}")

        return Response(status=status.HTTP_200_OK)


__all__ = ["BuiltHelperAPIView"]
