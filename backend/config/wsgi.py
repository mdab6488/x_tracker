# config/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
# config/wsgi.py (and asgi.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')  # For development
application = get_wsgi_application()
# config/wsgi.py (and asgi.py)