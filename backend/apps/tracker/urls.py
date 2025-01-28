from django.urls import path
from django.utils.module_loading import import_string

urlpatterns = [
    path('latest-posts/', import_string('tracker.views.LatestPostsView').as_view(), name='latest-posts'),
]