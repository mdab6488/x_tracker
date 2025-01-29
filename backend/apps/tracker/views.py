from rest_framework import viewsets, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.core.cache import cache
from .models import XAccount, XPost
from .serializers import XAccountSerializer, XPostSerializer


class XPostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing XPost instances with caching for optimized performance.
    """
    queryset = XPost.objects.select_related('account').all()
    serializer_class = XPostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['posted_at']
    ordering = ['-posted_at']

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """
        Returns the latest posts with caching enabled for 30 seconds.
        """
        # Try to get cached data
        cache_key = 'latest_posts'
        cached_data = cache.get(cache_key)
        
        if not cached_data:
            # If no cached data, query the database
            posts = self.get_queryset()[:100]  # Limit to the latest 100 posts
            serializer = self.get_serializer(posts, many=True)
            cached_data = serializer.data
            
            # Cache the data for 30 seconds
            cache.set(cache_key, cached_data, timeout=30)
        
        return Response(cached_data)


class LatestPostsView(generics.ListAPIView):
    """
    A generic view to retrieve the latest 100 posts, ordered by creation time.
    """
    serializer_class = XPostSerializer

    def get_queryset(self):
        """
        Dynamically fetches the latest 100 posts.
        """
        return XPost.objects.select_related('account').order_by('-created_at')[:100]
