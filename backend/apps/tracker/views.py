from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.core.cache import cache
from .models import XAccount, XPost
from .serializers import XAccountSerializer, XPostSerializer

class XPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = XPost.objects.all()
    serializer_class = XPostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['posted_at']
    ordering = ['-posted_at']

    @action(detail=False, methods=['get'])
    def latest(self, request):
        # Try to get cached data
        cache_key = 'latest_posts'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            # If no cached data, query the database
            posts = self.get_queryset().select_related('account')[:100]
            serializer = self.get_serializer(posts, many=True)
            cached_data = serializer.data
            
            # Cache the data for 30 seconds
            cache.set(cache_key, cached_data, 30)
        
        return Response(cached_data)

class LatestPostsView(generics.ListAPIView):
    serializer_class = XPostSerializer
    queryset = XPost.objects.all().order_by('-created_at')[:100]  # Get 100 latest posts
    
    def get_queryset(self):
        return self.queryset


