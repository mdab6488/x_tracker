from rest_framework import generics
from django.apps import apps

class LatestPostsView(generics.ListAPIView):
    serializer_class = None  # Will be set dynamically
    queryset = None  # Will be set dynamically

    def get_serializer_class(self):
        # Lazy import to avoid circular imports
        from .serializers import XPostSerializer
        return XPostSerializer

    def get_queryset(self):
        # Lazy import to avoid circular imports
        XPost = apps.get_model('tracker', 'XPost')
        return XPost.objects.order_by('-created_at')[:100]


