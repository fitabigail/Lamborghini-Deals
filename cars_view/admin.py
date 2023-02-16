from django.contrib import admin
from .models import Car
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html

# Register your models here.


@admin.register(Car)
class CarAdmin(SummernoteModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 10px" />'.format(obj.image.url))

    list_display = ('id', 'image_tag', 'car_title', 'model', 'fuel_type', 'body_style',)
    prepopulated_fields = {'slug': ('car_title',)}
    list_display_links = ('id', 'image_tag', 'car_title', 'model',)
    search_fields = ('model', 'fuel_type', 'body_style',)
    list_filter = ('model', 'fuel_type', 'body_style',)
    summernote_fields = ('description')

