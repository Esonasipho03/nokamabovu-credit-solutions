#!/usr/bin/env bash
# Render build step: install deps, collect static files, apply migrations.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# Create (or reset) the admin login from the Render environment variables
# DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD.
# Unlike plain createsuperuser, this also resets the password if the user
# already exists, so the login always matches what is set in Render.
if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
  python manage.py shell <<'PYEOF'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
u, created = User.objects.get_or_create(username=os.environ["DJANGO_SUPERUSER_USERNAME"])
u.email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
u.is_staff = True
u.is_superuser = True
u.is_active = True
u.set_password(os.environ["DJANGO_SUPERUSER_PASSWORD"])
u.save()
print("Admin user", "created" if created else "updated", ":", u.username)
PYEOF
else
  echo "DJANGO_SUPERUSER_USERNAME / DJANGO_SUPERUSER_PASSWORD not set - no admin user created."
fi
