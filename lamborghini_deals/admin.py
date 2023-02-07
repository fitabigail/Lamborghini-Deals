from django.contrib import admin
from .models import Team
from django_summernote.admin import SummernoteModelAdmin

# Register Team model here.


admin.site.register(Team)
