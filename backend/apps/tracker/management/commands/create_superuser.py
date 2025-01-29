# create_superuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates initial superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='x_tracker_user').exists():
            User.objects.create_superuser(
                username='x_tracker_user',
                password='alamin786',
                email='mdab6488@gmail.com'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))