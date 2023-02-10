from django.contrib import admin
from .models import Team
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html

# Register Team model here.


class TeamAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('id', 'image_tag', 'first_name', 'last_name', 'position_name', 'created_on',)    
    list_display_links = ('id', 'image_tag', 'first_name', 'last_name', 'position_name',)
    search_fields = ('first_name', 'last_name', 'position_name',)
    list_filter = ('position_name',)


admin.site.register(Team, TeamAdmin)
