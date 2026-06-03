import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Grab the credentials securely from Render's environment
ADMIN_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if ADMIN_PASSWORD:
    if not User.objects.filter(username=ADMIN_USERNAME).exists():
        User.objects.create_superuser(ADMIN_USERNAME, 'admin@example.com', ADMIN_PASSWORD)
        print("Superuser created securely!")
    else:
        print("Superuser already exists.")
else:
    print("Skipping superuser creation: DJANGO_SUPERUSER_PASSWORD not set.")
