from django.db import models

class XAccount(models.Model):
    username = models.CharField(max_length=255, unique=True)
    last_checked = models.DateTimeField(auto_now=True)
    latest_post_id = models.CharField(max_length=255, blank=True)

class XPost(models.Model):
    account = models.ForeignKey(XAccount, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)