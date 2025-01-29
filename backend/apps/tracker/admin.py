# backend/<app_name>/admin.py
from django.contrib import admin
from .models import XAccount, XPost  # Import your actual models

admin.site.register(XAccount)
admin.site.register(XPost)