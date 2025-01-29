# backend/health/views.py
from django.http import JsonResponse
from django.db import connection

def health_check(request):
    # Test database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "ok"})