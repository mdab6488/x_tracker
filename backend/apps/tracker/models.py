from django.db import models
from django.utils import timezone

class XAccount(models.Model):
    username = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255)
    last_checked = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class XPost(models.Model):
    account = models.ForeignKey(XAccount, on_delete=models.CASCADE, related_name='posts')
    post_id = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    posted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-posted_at']
        indexes = [
            models.Index(fields=['-posted_at']),
        ]

    def __str__(self):
        return f"{self.account.username} - {self.post_id}"