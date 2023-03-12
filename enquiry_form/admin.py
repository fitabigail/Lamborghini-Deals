from django.contrib import admin
from .models import EnquiryForm

# Register EnquiryForm models here.


class EquieryAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'car_title', 'email',)
    list_display_links = ('id', 'first_name', 'last_name',)
    search_fields = ('first_name', 'last_name', 'car_title ',)
    list_per_page = 30


admin.site.register(EnquiryForm, EquieryAdmin)