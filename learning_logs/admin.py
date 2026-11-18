
"""Register Learning Log models with the Django admin site."""

from django.contrib import admin

from .models import Topic, Entry


admin.site.register(Topic)
admin.site.register(Entry)
