from django.contrib import admin

from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """

    """

    list_display = ('__str__', 'slug', 'updated_at', 'created_at',)
