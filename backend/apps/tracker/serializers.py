from rest_framework import serializers
from .models import XPost

class XPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = XPost
        fields = ['post_id', 'content', 'created_at']