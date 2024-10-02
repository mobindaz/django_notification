# notifications/admin.py

from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('message',)
    ordering = ('-created_at',)

    # Optionally add custom styles here
    class Media:
        css = {
            'all': ('https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',)
        }
        js = ('https://code.jquery.com/jquery-3.5.1.slim.min.js', 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js', 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js')

admin.site.register(Notification, NotificationAdmin)
