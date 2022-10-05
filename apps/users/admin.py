# Django imports
from django.contrib import admin

# Local imports
from apps.users.models import User


admin.site.register(User)