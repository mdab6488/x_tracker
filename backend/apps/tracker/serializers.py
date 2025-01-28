from rest_framework import serializers
from .models import XAccount, XPost

class XAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = XAccount
        fields = ['id', 'username', 'display_name', 'last_checked', 'is_active']

class XPostSerializer(serializers.ModelSerializer):
    account = XAccountSerializer(read_only=True)

    class Meta:
        model = XPost
        fields = ['id', 'account', 'post_id', 'content', 'posted_at']