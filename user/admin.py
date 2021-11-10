from django.contrib import admin

# Register your models here.

from .models import Plants, Scrape

admin.site.register(Plants)
admin.site.register(Scrape)
