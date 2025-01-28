# from django.urls import path
# from django.utils.module_loading import import_string

# urlpatterns = [
#     path('latest-posts/', import_string('tracker.views.LatestPostsView').as_view(), name='latest-posts'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import XPostViewSet

router = DefaultRouter()
router.register(r'posts', XPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]